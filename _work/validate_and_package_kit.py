from pathlib import Path
from bs4 import BeautifulSoup
import json,hashlib,zipfile,struct,re
import soundfile as sf
import numpy as np
R=Path('/home/user/suno_gemini_kit'); P1=R/'PART_1_GEMINI';P2=R/'PART_2_STUDIO_ASSETS';W=Path('/home/user/_work/dark_kit')
a=json.loads((P2/'ASSET_INDEX.json').read_text())['assets']
assert len(a)==70 and len({r['id'] for r in a})==70
kfiles=list((P1/'KNOWLEDGE').glob('*.txt'))
assert len(kfiles)==6
assert len((P1/'GEM_INSTRUCTIONS.txt').read_text())<8000
assert (P1/'KNOWLEDGE'/'05_ASSET_CATALOG_AND_RECIPES.txt').read_text()==(P2/'ASSET_CATALOG_RU.md').read_text()

def vlq(data,p):
    n=0
    for _ in range(4):
        z=data[p];p+=1;n=(n<<7)|(z&127)
        if z<128:return n,p
    raise ValueError('invalid VLQ')

def midi_validate(path,rec):
    data=path.read_bytes();assert data[:4]==b'MThd'
    size,fmt,nt,ppq=struct.unpack('>IHHH',data[4:14]);assert (size,fmt,nt,ppq)==(6,1,2,480)
    p=14;notes=0;tempo=None;ends=[];keys=[];channels=set();maxpoly=0
    for tr in range(nt):
        assert data[p:p+4]==b'MTrk';ln=int.from_bytes(data[p+4:p+8],'big');block=data[p+8:p+8+ln];p+=8+ln
        j=0;t=0;active=set()
        while j<len(block):
            dt,j=vlq(block,j);t+=dt;st=block[j];j+=1
            if st==255:
                typ=block[j];j+=1;n,j=vlq(block,j);payload=block[j:j+n];j+=n
                if typ==81:tempo=int.from_bytes(payload,'big')
                if typ==89:keys.append(payload)
                if typ==47:assert n==0 and j==len(block)
            else:
                assert st&240 in (128,144)
                pitch,vel=block[j:j+2];j+=2;ch=st&15;channels.add(ch)
                if st&240==144 and vel:
                    assert (ch,pitch) not in active,(rec['id'],t,pitch)
                    active.add((ch,pitch));notes+=1;maxpoly=max(maxpoly,len(active))
                else:
                    assert (ch,pitch) in active
                    active.remove((ch,pitch))
        assert not active;ends.append(t)
    assert p==len(data) and notes==rec['note_count']
    assert ends==[rec['bars']*4*480]*2
    seconds=max(ends)/ppq*tempo/1e6
    assert abs(seconds-rec['duration_s'])<1e-5
    if rec['kind']=='gm_drum_midi':assert channels=={9} and not keys
    else:assert channels=={0} and keys
    if rec['role']=='Bass':assert maxpoly==1
    return {'id':rec['id'],'note_ons':notes,'max_polyphony':maxpoly,'duration_s':round(seconds,6),'valid':True}

reports=[]
for rec in a:
    p=P2/rec['path'];assert p.is_file()
    assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256'],rec['id']
    if p.suffix=='.wav':
        info=sf.info(p);data,sr=sf.read(p,always_2d=True)
        assert sr==48000 and info.subtype=='PCM_24'
        assert data.shape[1]==rec['channels'] and np.isfinite(data).all()
        assert np.max(np.abs(data))<.999 and np.sqrt(np.mean(data**2))>.00001
        assert np.max(np.abs(data[0]))<1e-6 and np.max(np.abs(data[-1]))<1e-6
        assert abs(len(data)/sr-rec['duration_s'])<1e-6
        if rec.get('bars'):assert abs(len(data)/sr-rec['bars']*4*60/rec['bpm'])<1/sr
        reports.append({'id':rec['id'],'format':'WAV PCM24/48000','samples':len(data),'digital_clipping':False,'valid':True})
    elif p.suffix=='.mid':reports.append(midi_validate(p,rec))
    else:assert rec['kind']=='recipe' and p.suffix=='.txt'

# Check all actual asset paths are represented in the knowledge inventory.
knowledge=(P1/'KNOWLEDGE'/'05_ASSET_CATALOG_AND_RECIPES.txt').read_text()
for rec in a:assert rec['file'] in knowledge and rec['path'] in knowledge
alltext='\n'.join(p.read_text() for p in kfiles)
assert 'v5.5 → v6' not in (Path('/home/user/START_HERE_GEMINI_STUDIO.html').read_text())
# No stale dependency on the old download bundle.
assert 'suno_v6_midi_starters_96bpm.zip' not in alltext
for f in [Path('/home/user/START_HERE_GEMINI_STUDIO.html'),P2/'BROWSE_LIBRARY.html']:
    soup=BeautifulSoup(f.read_text(),'html.parser')
    ids=[x['id'] for x in soup.find_all(id=True)];assert len(ids)==len(set(ids))
    assert not [x for x in soup.find_all(['img','script','link']) if x.get('src') or x.get('href')]
    assert all(x['href'][1:] in ids for x in soup.select('a[href^="#"]'))
    ad=json.loads(soup.find(id='audio-data').string);met=json.loads(soup.find(id='meta-data').string)
    for btn in soup.select('[data-play]'):assert btn['data-play'] in ad
    for btn in soup.select('[data-asset]'):assert btn['data-asset'] in met
    for btn in soup.select('[data-copy-target]'):assert btn['data-copy-target'] in ids
    if f.parent==P2:
        assert len(soup.select('.asset'))==70
        for x in soup.find_all('a',href=True):
            link=x['href']
            if not link.startswith(('http','#','data:')):assert (P2/link).exists(),link
    js='\n'.join(t.string or '' for t in soup.find_all('script') if t.get('type')!='application/json')
    js_path=W/(f.stem+'.js')
    js_path.write_text(js)
    import subprocess
    subprocess.run(['node','--check',str(js_path)],check=True,capture_output=True,text=True)

report={'version':'2026-09-11','knowledge_files':6,'gem_instruction_characters':len((P1/'GEM_INSTRUCTIONS.txt').read_text()),'wav':48,'midi':12,'recipes':10,'asset_total':70,'verified':['WAV encoding/length/finite samples/no digital clipping','4x true-peak estimates in index','MIDI structure, note lifetimes, monophonic bass, drum routing metadata','catalog paths and SHA256','knowledge catalog matches actual library','HTML local links, embedded audio refs and copy targets'], 'not_verified':['Import in user Suno account','Gemini custom Gem behavior in user account','Perceptual suitability in user song','Perfect artifact removal'], 'media':reports}
(P2/'VALIDATION_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
(W/'FINAL_QA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
for folder in [P1,P2]:
    lines=[]
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.name!='CHECKSUMS.sha256':lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(folder).as_posix())
    (folder/'CHECKSUMS.sha256').write_text('\n'.join(lines)+'\n')
    zp=Path('/home/user')/(folder.name+'.zip')
    with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(folder.rglob('*')):
            if p.is_file():z.write(p,folder.name+'/'+p.relative_to(folder).as_posix())
    with zipfile.ZipFile(zp) as z:
        assert z.testzip() is None
        assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
        print(zp.name,'files=',len(z.namelist()),'MiB=',round(zp.stat().st_size/1024**2,2))
print('PASS: package and media validation complete; user-account tests intentionally not claimed.')
