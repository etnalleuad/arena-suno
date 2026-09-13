from pathlib import Path
import numpy as np
import scipy.signal as sig
import soundfile as sf
import struct, json, csv, hashlib, io, wave, base64, math, re

ROOT=Path('/home/user/suno_gemini_kit')
P2=ROOT/'PART_2_STUDIO_ASSETS'
P2.mkdir(parents=True,exist_ok=True)
WORK=Path('/home/user/_work/dark_kit')
WORK.mkdir(parents=True,exist_ok=True)
FS=48000
PPQ=480
rng=np.random.default_rng(11092026)
assets=[]
raw={}
previews={}
notes_store={}


def db(x): return float(20*np.log10(max(float(x),1e-12)))
def time(d): return np.arange(round(d*FS))/FS

def filt(x,cut,kind='lowpass',order=3):
    return sig.sosfilt(sig.butter(order,cut,btype=kind,fs=FS,output='sos'),x,axis=0)

def fades(x,attack=.002,release=.014):
    x=np.array(x,dtype=np.float64,copy=True)
    na=min(round(attack*FS),len(x)//4);nr=min(round(release*FS),len(x)//3)
    if na>0:
        e=np.sin(np.linspace(0,np.pi/2,na))**2
        x[:na]*=e[:,None] if x.ndim==2 else e
    if nr>0:
        e=np.cos(np.linspace(0,np.pi/2,nr))**2
        x[-nr:]*=e[:,None] if x.ndim==2 else e
    return x

def noise(d,lo=100,hi=13000):
    x=rng.normal(0,1,round(d*FS))
    return filt(x,[lo,hi],'bandpass',2)

def norm(x,peak=-7):
    x=np.asarray(x,dtype=np.float64)
    x=filt(x,13,'highpass',2)
    x=filt(x,18500,'lowpass',3)
    x=fades(x)
    p=max(np.max(np.abs(x)),1e-12)
    x=x*(10**(peak/20)/p)
    tp=np.max(np.abs(sig.resample_poly(x,4,1,axis=0)))
    if tp>10**(-4/20):x*=10**(-4/20)/tp
    return x

def pan(x,p=0):
    if np.asarray(x).ndim==2:return x
    a=(p+1)*np.pi/4
    return np.column_stack([x*np.cos(a),x*np.sin(a)])

def add(dst,src,start=0,gain=1,p=0,circular=False):
    src=np.asarray(src)*gain
    if dst.ndim==2 and src.ndim==1:src=pan(src,p)
    if dst.ndim==1 and src.ndim==2:src=np.mean(src,axis=1)
    i=round(start*FS)
    if circular:
        for pos in range(0,len(src),len(dst)):
            ss=src[pos:pos+len(dst)]
            j=(i+pos)%len(dst)
            a=min(len(ss),len(dst)-j)
            dst[j:j+a]+=ss[:a]
            if a<len(ss):dst[:len(ss)-a]+=ss[a:]
    else:
        if i<0:src=src[-i:];i=0
        a=min(len(src),len(dst)-i)
        if a>0:dst[i:i+a]+=src[:a]


def preview(x):
    mono=np.mean(x,axis=1) if x.ndim==2 else x
    mono=mono[:round(5*FS)]
    y=sig.resample_poly(mono,147,320)
    y=fades_preview(y,22050)
    b=io.BytesIO()
    with wave.open(b,'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(22050)
        w.writeframes((np.clip(y,-1,.999969)*32767).astype('<i2').tobytes())
    return base64.b64encode(b.getvalue()).decode()

def fades_preview(x,sr):
    y=x.copy(); n=min(len(y)//4,int(.012*sr))
    if n:
        y[:n]*=np.sin(np.linspace(0,np.pi/2,n))**2
        y[-n:]*=np.cos(np.linspace(0,np.pi/2,n))**2
    return y


def store_audio(aid,slug,x,role,desc,folder,bpm=None,key=None,bars=None,kind='one_shot',related=None,pitch=None,scene=False):
    x=norm(x,-9 if scene else -7)
    p=P2/'AUDIO'/folder/f'{aid}_{slug}.wav';p.parent.mkdir(parents=True,exist_ok=True)
    # Tiny TPDF dither for PCM24; fades leave clean endpoints.
    dither=(rng.random(x.shape)-rng.random(x.shape))/2**24
    z=x+dither;z[0]=0;z[-1]=0
    sf.write(p,z,FS,subtype='PCM_24',format='WAV')
    read,sr=sf.read(p,dtype='float64',always_2d=True)
    assert sr==FS and np.isfinite(read).all() and len(read)>10
    tp=db(np.max(np.abs(sig.resample_poly(read,4,1,axis=0))))
    assert tp < -3.8,(aid,tp)
    rec={
        'id':aid,'file':p.name,'path':p.relative_to(P2).as_posix(),'kind':kind,
        'role':role,'description_ru':desc,'sample_rate':FS,'bit_depth':24,
        'channels':read.shape[1],'duration_s':round(len(read)/FS,6),'bpm':bpm,
        'key':key,'bars':bars,'root_note':pitch,'peak_dbfs':round(db(np.max(np.abs(read))),2),
        'true_peak_dbfs_4x':round(tp,2),'rms_dbfs':round(db(np.sqrt(np.mean(read**2))),2),
        'dc_mean':round(float(np.mean(read)),9),'related':related or [],
        'destination':'Studio Audio track / local DAW Audio track',
        'not_destination':'Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.',
        'usage_ru':('Полный инструментальный эскиз. Audio/reference, НЕ изолированный stem. Не смешивать со всеми его компонентами без намерения.' if scene else ('Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.' if kind=='loop' else 'Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.')),
        'source':'original_procedural_synthesis','third_party_audio':False,'contains_human_voice':False,
        'ai_source_status':'Original package material; check target service conditions; not a Voice training sample.',
        'sha256':hashlib.sha256(p.read_bytes()).hexdigest()
    }
    assets.append(rec);raw[aid]=x;previews[aid]=preview(x)
    print(aid,p.name,round(p.stat().st_size/1024), 'KB',flush=True)
    return rec

# 12 dry synthetic percussion one-shots.
t=time(.65);phase=2*np.pi*(50*t+(.0+88)*.018*(1-np.exp(-t/.018)))
k=np.sin(phase)*np.exp(-t/ .14)+.13*noise(.65,1200,9500)*np.exp(-t/.007)
store_audio('D01','DeepShortKick',np.tanh(1.4*k),'Drums','Короткий плотный синтетический kick; не длинный басовый дроп.','01_Drums')
t=time(.45);s=.5*noise(.45,500,14500)*np.exp(-t/.078)+(.6*np.sin(2*np.pi*186*t)+.17*np.sin(2*np.pi*329*t))*np.exp(-t/.048)
store_audio('D02','DryBodySnare',s,'Drums','Сухой snare с телом и коротким шумовым хвостом.','01_Drums')
t=time(.22);s=(np.sin(2*np.pi*760*t)+.55*np.sin(2*np.pi*1530*t)+.18*noise(.22,1400,14500))*np.exp(-t/.031)
store_audio('D03','SkinRim',s,'Drums','Узкий rim-акцент; заполнять редкие паузы, не весь ритм.','01_Drums')
for aid,slug,d,decay,lo in [('D04','ClosedSteelHat',.13,.022,6500),('D05','OpenDustHat',.48,.105,4600),('D06','SoftShake',.22,.05,3400)]:
 t=time(d);s=noise(d,lo,16500)*np.exp(-t/decay)
 if aid=='D06':s*=.4+.6*np.sin(np.pi*np.clip(t/.07,0,1))
 store_audio(aid,slug,s,'Drums',{'D04':'Короткий закрытый hat.','D05':'Умеренно длинный пыльный hat.','D06':'Лёгкий шумовой shaker-акцент.'}[aid],'01_Drums')
t=time(.38);s=np.zeros(len(t))
for st,g in [(0,.7),(.012,.5),(.029,.8),(.047,.25)]:
 q=time(.30);add(s,noise(.30,800,8500)*np.exp(-q/.055),st,g)
store_audio('D07','BrokenClap',s,'Drums','Небольшой расслаивающийся clap; не стадионный хлопок.','01_Drums')
t=time(.6);phase=2*np.pi*(88*t+30*.045*(1-np.exp(-t/.045)))
store_audio('D08','LowOrganicTom',np.sin(phase)*np.exp(-t/.14)+.045*noise(.6,350,4000)*np.exp(-t/.02),'Drums','Низкий синтетический tom с короткой мягкой атакой.','01_Drums')
t=time(.22);s=(np.sin(2*np.pi*510*t)+.7*np.sin(2*np.pi*921*t)+.24*np.sin(2*np.pi*1720*t))*np.exp(-t/.024)
store_audio('D09','ThinWoodKnock',s,'Percussion','Синтезированный wood-like knock. Это не живая field recording.','01_Drums')
t=time(.25);s=sum(np.sin(2*np.pi*f*t)*np.exp(-t/tau)*g for f,tau,g in [(1110,.023,1),(2370,.018,.55),(3997,.011,.3)])
store_audio('D10','MetalRimTick',s,'Percussion','Тонкий металлический tick для междолевых акцентов.','01_Drums')
t=time(.7);s=noise(.7,850,13500)*np.sin(np.pi*np.minimum(t/.7,1))**2*np.exp(-t/.45)
store_audio('D11','BrushScrape',s,'Percussion','Синтетический короткий шорох; располагать в паузах вокала.','01_Drums')
t=time(.45);s=(np.sin(2*np.pi*116*t)+.25*np.sin(2*np.pi*179*t))*np.exp(-t/.063)+.12*noise(.45,180,2500)*np.exp(-t/.027)
store_audio('D12','MutedThud',s,'Percussion','Приглушённый тактильный удар без большого сабового хвоста.','01_Drums')

# 12 electrical / organic synthetic effects.
t=time(.2);s=(np.sin(2*np.pi*2050*t)+.45*np.sin(2*np.pi*3187*t))*np.exp(-t/.009)+.22*noise(.2,2400,14500)*np.exp(-t/.025)
store_audio('F01','RelayClick',s,'FX','Короткий relay click для механического рисунка.','02_Electric_FX')
t=time(.42);s=noise(.42,900,17000)*np.exp(-t/.028)*(1+.35*np.sin(2*np.pi*570*t))+.08*np.sin(2*np.pi*280*t)*np.exp(-t/.055)
store_audio('F02','ElectricalCrack',s,'FX','Хлёсткий короткий электрический crack без голоса и ритма.','02_Electric_FX')
s=np.zeros(round(.75*FS))
for i,st in enumerate([0,.041,.09,.137,.202,.277,.359,.467]):add(s,raw['F01'],st,.8-i*.055)
store_audio('F03','RatchetBurst',s,'FX','Неровная цепочка relay-щелчков; одиночный жест, не музыкальный луп.','02_Electric_FX')
t=time(1.3);s=noise(1.3,700,8000)*(np.sin(np.pi*t/1.3)**2)*(.3+.7*np.sin(2*np.pi*37*t)**2)
s+=.12*np.sin(2*np.pi*(780*t+125*t*t))*np.sin(np.pi*t/1.3)**2
store_audio('F04','WireScrape',s,'FX','Шероховатый wire-like scrape с меняющейся окраской.','02_Electric_FX')
t=time(.55);s=noise(.55,1900,14500)*np.exp(-t/.105)*(.5+.5*np.sin(2*np.pi*83*t))
store_audio('F05','BandlimitedSpark',s,'FX','Искристый ограниченный по полосе шумовой акцент.','02_Electric_FX')
s=np.zeros(round(1.25*FS))
for st,g in [(0,.8),(.11,.34),(.188,.65),(.42,.5),(.447,.35),(.66,.22),(.91,.5)]:add(s,raw['F02'],st,g)
store_audio('F06','ShortCircuitStutter',s,'FX','Один рваный электрический stutter; не обещает попадание в любую сетку.','02_Electric_FX')
t=time(2);s=sum(g*np.sin(2*np.pi*f*t)*np.exp(-t/tau) for f,tau,g in [(310,.65,1),(733,.5,.7),(1493,.35,.35)])
store_audio('F07','ReverseMetalSwell',s[::-1],'FX','Обратный металлический подвод к событию; окончание совместить со стыком.','02_Electric_FX')
t=time(1.6);s=sum(g*np.sin(2*np.pi*f*t)*np.exp(-t/tau) for f,tau,g in [(127,.6,.8),(397,.42,.5),(937,.25,.23)])
store_audio('F08','CableResonance',s,'FX','Резонансный кабельный жест; материал синтезирован, не записан в поле.','02_Electric_FX')
t=time(1.4);s=noise(1.4,500,14500)*.25
for a,b in [(.1,.25),(.44,.59),(.84,1.1)]:s[(t>a)&(t<b)]*=.025
store_audio('F09','StaticDropout',s,'FX','Шумовая текстура с провалами; содержит намеренные dropout, не дефект файла.','02_Electric_FX')
t=time(2.5);s=noise(2.5,2300,12500)*np.sin(np.pi*t/2.5)**2*(.65+.35*np.sin(2*np.pi*5.3*t))
store_audio('F10','AirShiver',s,'FX','Воздушная синтетическая дрожь. Не человеческий вдох и не вокал.','02_Electric_FX')
t=time(1.2);s=np.sin(2*np.pi*36.7081*t)*np.exp(-t/.29)+.04*noise(1.2,700,6000)*np.exp(-t/.017)
store_audio('F11','SubImpact_D1',s,'FX','Низкий D1 impact; не накладывать без проверки на саб и kick.','02_Electric_FX',pitch='D1')
t=time(1.1);inst=310*np.exp(-t/ .37)+30;ph=2*np.pi*np.cumsum(inst)/FS
s=(np.sin(ph)+.25*np.sin(ph*2.07))*np.sin(np.pi*np.minimum(t/1.1,1))**.5
store_audio('F12','TapeStopGesture',s,'FX','Синтетическое замедление высоты для конца фразы; не реальная лента.','02_Electric_FX')


def hz(note):return 440*2**((note-69)/12)
def synth(note,gate,kind='tines',vel=80):
    tail={'bass':.11,'tines':.28,'pad':.5,'glass':.6,'string':.2,'edge':.1}.get(kind,.2)
    d=gate+tail;t=time(d);f=hz(note)
    if kind in ['bass','edge']:
        s=np.sin(2*np.pi*f*t)+.14*np.sin(4*np.pi*f*t)+.035*np.sin(6*np.pi*f*t)
        if kind=='edge':s=np.tanh(s*3.2);s=filt(s,170,'highpass',2)
        e=np.minimum(t/.006,1)*(.88+.12*np.exp(-t/.18))
    elif kind=='tines':
        idx=2.1*np.exp(-t/.095)
        s=np.sin(2*np.pi*f*t+idx*np.sin(2*np.pi*f*2.002*t))
        s+=.19*np.sin(2*np.pi*f*4.03*t)*np.exp(-t/.10)
        e=np.minimum(t/.007,1)*(.78*np.exp(-t/1.25)+.22*np.exp(-t/.12))
    elif kind=='glass':
        s=sum(g*np.sin(2*np.pi*f*r*t)*np.exp(-t/tau) for r,g,tau in [(1,1,1.3),(2.76,.35,.65),(4.81,.19,.38),(6.11,.10,.2)])
        e=np.minimum(t/.007,1)
    elif kind=='string':
        s=sum(np.sin(2*np.pi*f*i*t+(.008*i)*np.sin(2*np.pi*1.7*t))*np.exp(-t/(.9/(1+i*.14)))/(i**1.45) for i in range(1,10))
        e=np.minimum(t/.003,1)
    else:
        s=sum((np.sin(2*np.pi*f*r*t)+.6*np.sin(2*np.pi*f*r*1.0022*t))/(r**1.6) for r in [1,2,3,4,5])
        e=np.minimum(t/.28,1)*(.82+.18*np.sin(2*np.pi*.11*t))
    after=t>gate
    e[after]*=np.maximum(0,1-(t[after]-gate)/tail)**2
    return fades(s*e*(vel/127),.002,.008)

for aid,slug,n,g,k in [('N01','Sub_D2',38,.9,'bass'),('N02','Sub_E2',40,.9,'bass'),('N03','Sub_Fsharp1',30,1.1,'bass'),('N04','Sub_A1',33,.9,'bass'),('N05','Tine_D4',62,1.8,'tines'),('N06','Glass_A4',69,2.2,'glass'),('N07','MutedKey_E4',64,1.35,'tines'),('N08','MetalTone_D3',50,1.45,'glass'),('N09','SyntheticString_E3',52,1.3,'string')]:
    role='Bass' if k=='bass' else ('Synth string' if k=='string' else 'Keys')
    store_audio(aid,slug,synth(n,g,k),role,f'Одиночная синтезированная нота {slug.split("_",1)[-1]}; менять высоту осмысленно, не путать с аккордовым лупом.','03_Pitched_OneShots',pitch=slug.split('_')[-1],related=['R01'] if k=='bass' else ['R03'])

# Standard MIDI Type 1 writer + independent event verifier.
def vlq(n):
 b=[n&127]
 while n>>7:n>>=7;b.insert(0,(n&127)|128)
 return bytes(b)
def meta(t,p):return bytes([255,t])+vlq(len(p))+p

def midi_write(aid,slug,notes,bpm,bars,key,role,desc,ch=0,related=None,gm=False):
    total=bars*4*PPQ;tempo=round(60e6/bpm)
    ks={'D minor':(-1,1),'E minor':(1,1),'F-sharp minor':(3,1)}[key]
    def tr(events):
        out=b'';last=0
        for tick,order,msg in sorted(events,key=lambda e:(e[0],e[1])):
            assert tick>=last
            out+=vlq(tick-last)+msg;last=tick
        out+=vlq(total-last)+meta(47,b'')
        return b'MTrk'+struct.pack('>I',len(out))+out
    conductor=[(0,0,meta(3,b'Dark production toolkit')),(0,1,meta(81,tempo.to_bytes(3,'big'))),(0,2,meta(88,bytes([4,2,24,8])))]
    if not gm: conductor.append((0,3,meta(89,bytes([ks[0]%256,ks[1]]))))
    t0=tr(conductor)
    events=[(0,-1,meta(3,f'{aid} {role}'.encode('ascii')))]
    for start,dur,pitch,vel in notes:
        st=round(start*PPQ);en=round((start+dur)*PPQ)
        assert 0<=st<en<=total and 0<=pitch<128 and 0<vel<128
        events.extend([(st,1,bytes([0x90|ch,pitch,vel])),(en,0,bytes([0x80|ch,pitch,0]))])
    data=b'MThd'+struct.pack('>IHHH',6,1,2,PPQ)+t0+tr(events)
    p=P2/'MIDI'/f'{aid}_{slug}.mid';p.parent.mkdir(exist_ok=True);p.write_bytes(data)
    notes_store[aid]=(notes,bpm,bars,key)
    assets.append({'id':aid,'file':p.name,'path':p.relative_to(P2).as_posix(),'kind':'gm_drum_midi' if gm else 'midi','role':role,'description_ru':desc,'duration_s':round(tempo/1e6*4*bars,6),'bpm':bpm,'key':None if gm else key,'bars':bars,'note_count':len(notes),'pitch_min':min(x[2] for x in notes),'pitch_max':max(x[2] for x in notes),'midi_channel_1based':ch+1,'related':related or [],'destination':'External DAW + mapped drum sampler only' if gm else 'Studio MIDI track + Wavetable / external DAW MIDI instrument','not_destination':'Default Wavetable is NOT a GM drum kit; use paired WAV loop in Suno.' if gm else 'Not an Audio WAV clip or FX preset. MIDI has no stored sound.','usage_ru':'Только DAW с drum-map или сопоставлением своих one-shot. В Suno удобнее связанный WAV-луп.' if gm else 'Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.','source':'original_composed_midi','third_party_audio':False,'contains_human_voice':False,'sha256':hashlib.sha256(data).hexdigest()})
    return data

# These are the same musical ideas as the previous two eight-bar examples.
bpat=[(0,0,1.8,38,82),(0,2.5,.6,38,72),(1,0,2.6,38,81),(1,3.5,.35,45,65),(2,0,1.75,34,84),(2,2.75,.5,41,68),(3,0,3.15,34,80),(3,3.5,.25,34,64),(4,0,1.8,31,83),(4,2.5,.75,38,72),(5,0,2.5,31,80),(5,3,.6,38,66),(6,0,2.25,33,82),(6,3,.75,33,70),(7,0,1.8,33,82),(7,2.75,.5,37,67),(7,3.5,.35,33,74)]
bass=[(b*4+t,d,n,v) for b,t,d,n,v in bpat]
chords=[[53,57,62,64]]*2+[[53,57,58,62]]*2+[[55,58,62,69]]*2+[[57,62,64,69],[57,61,64,69]]
hits=[[(.5,1.75,57),(3.25,.5,48)],[(1,2,53)],[(.5,1.75,55),(3,.5,47)],[(.75,2.25,52)],[(.5,1.5,56),(3.25,.5,46)],[(1,2,51)],[(.5,2.5,54)],[(0,2,55),(3,.5,45)]]
keys=[(b*4+st,d,n,v+[-3,1,-1,3][j]) for b,(chord,hh) in enumerate(zip(chords,hits)) for st,d,v in hh for j,n in enumerate(chord)]
midi_write('M01','Keys_Dm_96_8bars',keys,96,8,'D minor','Keys','Редкие Dm(add9)/Bbmaj7/Gm(add9)/Asus4/A voicings; пара к L04. C-sharp в финальном A намеренный.',related=['L04','R03'])
midi_write('M02','Bass_Dm_96_8bars',bass,96,8,'D minor','Bass','Монофонический бас к M01; пара к L03.',related=['L03','R01'])

def chord_notes(voicings,offset=.5,gate=2.0):
 return [(b*4+offset,gate,n,52+j*2+(b%2)*3) for b,cc in enumerate(voicings) for j,n in enumerate(cc)]
ke=chord_notes([[55,59,64,66],[55,59,60,64],[54,57,62,66],[57,59,63,66]])
be=[(b*4,2.2,n,79) for b,n in enumerate([40,36,38,35])]+[(b*4+3.0,.5,n,66) for b,n in enumerate([47,43,45,42])]
midi_write('M03','Keys_Em_102_4bars',ke,102,4,'E minor','Keys','Разреженные клавишные Em/Cmaj7/D/B для альтернативного indie.',related=['L09','R03'])
midi_write('M04','Bass_Em_102_4bars',be,102,4,'E minor','Bass','Опорный бас Em-палитры; B как доминанта содержит D-sharp в keys.',related=['L08','R01'])
kf=chord_notes([[57,61,66,68],[57,61,62,66],[56,59,64,68],[56,61,65,68]],.25,2.25)
midi_write('M05','GlassChords_Fsm_100_4bars',kf,100,4,'F-sharp minor','Keys','Стеклянная F-sharp minor-палитра: F#m/D/E/C#.',related=['L11','R04'])
pad=chord_notes([[57,62,64,69],[57,62,64,69],[57,58,62,65],[57,58,62,65]],0,3.5)
midi_write('M06','Pad_Dm_96_4bars',pad,96,4,'D minor','Pad','Верхняя подложка Dm/Bb, без басового регистра.',related=['L05','R04'])
string=[(b*4+st,.5,n,62+(j%3)*5) for b,nn in enumerate([[52,55,59],[52,55,60],[54,57,62],[54,59,63]]) for j,(st,n) in enumerate(zip([.75,2.0,3.25],nn))]
midi_write('M07','StringCounter_Em_102_4bars',string,102,4,'E minor','Synth string','Контрлиния для синтетического щипкового тембра; это не запись гитариста.',related=['L10','N09'])
motif=[(b*4+st,d,n,60+j*4) for b in range(4) for j,(st,d,n) in enumerate([(.5,.75,69),(2,.5,65),(3,.65,64 if b<2 else 62)])]
midi_write('M08','SparseMotif_Dm_96_4bars',motif,96,4,'D minor','Lead','Небольшой высокий мотив в паузах; не конкурировать с голосом.',related=['N06','R03'])

def drum_events(bpm=96,alt=False):
 ev=[]
 for b in range(4):
  for pos,vel in ([(0,95),(2.5,75),(3.5,60)] if b%2==0 else [(0,90),(1.75,63)]):ev.append((b*4+pos,.12,36,vel))
  for pos in [1,3]:
   if not(alt and b==3 and pos==3):ev.append((b*4+pos,.12,38,84))
  for j,pos in enumerate([.5,1.5,2,2.75,3.5]):
   if (b+j)%5:ev.append((b*4+pos,.08,42,43+(j*7)%22))
 return ev
md=drum_events()
mp=[(b*4+pos,.08,n,52+(j*7)%20) for b in range(4) for j,(pos,n) in enumerate([(.25,75),(1.75,37),(2.25,76),(3.5,75)]) if not (b==2 and j==1)]
midi_write('M09','Drums_GM_96_4bars',md,96,4,'D minor','Drums','GM channel 10. Kick36/snare38/hat42. Не проигрывать обычным Wavetable как готовый kit.',ch=9,related=['L01','D01','D02','D04','R10'],gm=True)
midi_write('M10','Percussion_Map_96_4bars',mp,96,4,'D minor','Percussion','Channel10: 75→F01,37→D10,76→D09. Пользовательское сопоставление в DAW обязательно.',ch=9,related=['L02','R10'],gm=True)
bf=[(b*4,2.5,n,79) for b,n in enumerate([30,38,40,37])]+[(b*4+3.25,.45,n,64) for b,n in enumerate([37,45,47,44])]
midi_write('M11','Sub_Fsm_100_4bars',bf,100,4,'F-sharp minor','Bass','Низкая опора для F-sharp minor; для тихих динамиков добавить умеренные гармоники.',related=['N03','L11','R01'])
arp=[(b*4+st,.32,n,48+j*5) for b,nn in enumerate([[62,65,69,76],[62,69,65,74],[58,62,65,69],[58,65,62,74]]) for j,(st,n) in enumerate(zip([.5,1.25,2.5,3.25],nn))]
midi_write('M12','GlassArp_Dm_96_4bars',arp,96,4,'D minor','Keys','Разреженный glass-arp; точный рисунок можно менять в piano roll.',related=['N06','R04'])


def render_midi(mid,kind='tines',stereo=False):
 notes,bpm,bars,key=notes_store[mid];q=60/bpm
 x=np.zeros((round(bars*4*q*FS),2)) if stereo else np.zeros(round(bars*4*q*FS))
 for i,(st,d,n,v) in enumerate(notes):
  add(x,synth(n,d*q,kind,v),st*q,.7,(-.33 if n%2 else .33) if stereo else 0,circular=True)
 return x

def render_drums(events,bpm,stereo=False,mapping=None):
 q=60/bpm;x=np.zeros((round(16*q*FS),2)) if stereo else np.zeros(round(16*q*FS))
 mapping=mapping or {36:'D01',38:'D02',42:'D04'}
 for st,d,n,v in events:add(x,raw[mapping[n]],st*q,v/127,0 if n in [36,38] else .22,circular=True)
 return x

store_audio('L01','Drums_Broken_96_4bars',render_drums(md,96),'Drums','Изолированный broken-drum loop; соответствует M09.','04_Loops',96,None,4,'loop',['M09','D01','D02','D04'])
store_audio('L02','Perc_Machine_96_4bars',render_drums(mp,96,True,{75:'F01',37:'D10',76:'D09'}),'Percussion','Редкий механический слой без гармонии; соответствует M10.','04_Loops',96,None,4,'loop',['M10','F01','D10','D09'])
store_audio('L03','Sub_Dm_96_8bars',render_midi('M02','bass'),'Bass','Восемь тактов bass-only. MIDI M02 сохраняет редактируемые ноты.','04_Loops',96,'D minor',8,'loop',['M02','R01'])
store_audio('L04','Tines_Dm_96_8bars',render_midi('M01','tines',True),'Keys','Восемь тактов изолированных synthetic tines. НЕ гитара и не акустический рояль.','04_Loops',96,'D minor',8,'loop',['M01','R03'])
store_audio('L05','Pad_Thin_Dm_96_4bars',render_midi('M06','pad',True),'Pad','Тонкая верхняя подложка для пары Dm/Bb.','04_Loops',96,'D minor',4,'loop',['M06','R04'])
x=np.zeros((round(10*FS),2))
for st,aid,g,p in [(1.1,'F01',.7,-.5),(2.2,'F04',.28,.35),(4.65,'F02',.5,.1),(6.2,'F10',.18,-.25),(8.4,'F03',.3,.45)]:add(x,raw[aid],st,g,p,True)
store_audio('L06','ElectricalBed_96_4bars',x,'FX','Редкие электрические события на сетке96; без нотного ансамбля.','04_Loops',96,None,4,'loop',['F01','F02','F04','F10'])
store_audio('L07','Drums_Organic_90_4bars',render_drums(drum_events(90,True),90,mapping={36:'D12',38:'D03',42:'D06'}),'Drums','Более лёгкий organic-пульс90, без trap rolls.','04_Loops',90,None,4,'loop',['D12','D03','D06'])
store_audio('L08','Sub_Em_102_4bars',render_midi('M04','bass'),'Bass','Четырёхтактовый bass-only Em/C/D/B.','04_Loops',102,'E minor',4,'loop',['M04','R01'])
store_audio('L09','Keys_Em_102_4bars',render_midi('M03','tines',True),'Keys','Synthetic electric keys для альтернативного indie; пара к M03.','04_Loops',102,'E minor',4,'loop',['M03','R03'])
store_audio('L10','SyntheticString_Em_102_4bars',render_midi('M07','string',True),'Synth string','Синтетическая щипковая контрлиния, не живая гитарная запись.','04_Loops',102,'E minor',4,'loop',['M07','N09'])
store_audio('L11','Glass_Fsm_100_4bars',render_midi('M05','glass',True),'Keys','Хрупкая glass-палитра F#m/D/E/C#.','04_Loops',100,'F-sharp minor',4,'loop',['M05','M11','R04'])
store_audio('L12','Perc_Omissions_100_4bars',render_drums(drum_events(100,True),100,True,{36:'D08',38:'D09',42:'D10'}),'Percussion','Сетка100 с намеренными пропусками; не готовая полная drum-section.','04_Loops',100,None,4,'loop',['D08','D09','D10'])
# Original instrumental sketches, explicitly not isolated stems and not mastered songs.
def scene(parts,n):
 x=np.zeros((n,2))
 for aid,g,p in parts:
  a=raw[aid]
  if len(a)<n:a=np.tile(a,(math.ceil(n/len(a)),1)) if a.ndim==2 else np.tile(a,math.ceil(n/len(a)))
  add(x,a[:n],0,g,p)
 return x
n=round(10*FS)
s=scene([('L01',.56,0),('L02',.21,0),('L03',.40,0),('L04',.47,0),('L06',.24,0)],n)
store_audio('S01','ArtPop_Dm_96_4bars',s,'Scene','Инструментальный синтетический эскиз Dm96; место под собственный вокал. НЕ один stem.','05_Scene_Sketches',96,'D minor',4,'scene',['L01','L02','L03','L04','L06'],scene=True)
n=round(16*60/102*FS)
s=scene([('L08',.48,0),('L09',.43,0),('L10',.30,0)],n)
add(s,render_drums(md,102),0,.58)
store_audio('S02','IndiePulse_Em_102_4bars',s,'Scene','Синтетическая indie-подложка Em102. Щипковая партия не является живой гитарой.','05_Scene_Sketches',102,'E minor',4,'scene',['L08','L09','L10','M09'],scene=True)
n=round(9.6*FS)
s=scene([('L11',.44,0),('L12',.37,0)],n)
add(s,render_midi('M11','bass'),0,.66);add(s,raw['F02'],1.2,.21,-.15);add(s,raw['F06'],6.8,.15,.4)
store_audio('S03','IndustrialGlass_Fsm_100_4bars',s,'Scene','Контрастный industrial/glass-эскиз F#m100, без голоса. НЕ набор извлечённых стемов Suno.','05_Scene_Sketches',100,'F-sharp minor',4,'scene',['L11','L12','M11','F02','F06'],scene=True)

assert len([a for a in assets if a['path'].endswith('.wav')])==48
assert len([a for a in assets if a['path'].endswith('.mid')])==12
(WORK/'assets_media.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2))
(WORK/'preview_audio.json').write_text(json.dumps(previews))
# Numbers needed for catalog cards, and exact musical event records for audit.
(WORK/'midi_notes.json').write_text(json.dumps({k:{'notes':v[0],'bpm':v[1],'bars':v[2],'key':v[3]} for k,v in notes_store.items()},indent=2))
print('DONE',len(assets),'media assets',sum((P2/a['path']).stat().st_size for a in assets)/1024**2,'MiB',flush=True)
