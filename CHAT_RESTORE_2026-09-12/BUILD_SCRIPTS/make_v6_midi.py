from pathlib import Path
import struct
import zipfile
import json

ROOT = Path('/home/user')
OUT = ROOT / '_work' / 'v6_midi_starters'
OUT.mkdir(parents=True, exist_ok=True)
PPQ=480
TOTAL=8*4*PPQ
TEMPO=625000

def vlq(n):
    b=[n & 127]
    while n >> 7:
        n >>= 7
        b.insert(0,(n & 127)|128)
    return bytes(b)

def meta(t, data):
    return bytes([255,t])+vlq(len(data))+data

def chunk(events):
    buf=b''
    last=0
    for tick, order, data in sorted(events, key=lambda e:(e[0],e[1])):
        buf+=vlq(tick-last)+data
        last=tick
    buf+=vlq(TOTAL-last)+meta(47,b'')
    return b'MTrk'+struct.pack('>I',len(buf))+buf

def make(path,name,notes):
    conductor=[
        (0,0,meta(3,b'96 BPM - D minor - 8 bars')),
        (0,1,meta(81,TEMPO.to_bytes(3,'big'))),
        (0,2,meta(88,bytes([4,2,24,8]))),
        (0,3,meta(89,bytes([255,1]))),
        (0,4,meta(1,b'Original educational MIDI sketch. No audio or Suno generation.')),
    ]
    events=[(0,-1,meta(3,name.encode('ascii')))]
    for start, dur, pitch, vel in notes:
        s=round(start*PPQ);e=round((start+dur)*PPQ)
        assert 0<=s<e<=TOTAL
        assert 0<=pitch<=127 and 1<=vel<=127
        events += [(s,1,bytes([0x90,pitch,vel])),(e,0,bytes([0x80,pitch,0]))]
    file=b'MThd'+struct.pack('>IHHH',6,1,2,PPQ)+chunk(conductor)+chunk(events)
    path.write_bytes(file)

bass_pattern=[
    (0,0,1.8,38,82),(0,2.5,.6,38,72),
    (1,0,2.6,38,81),(1,3.5,.35,45,65),
    (2,0,1.75,34,84),(2,2.75,.5,41,68),
    (3,0,3.15,34,80),(3,3.5,.25,34,64),
    (4,0,1.8,31,83),(4,2.5,.75,38,72),
    (5,0,2.5,31,80),(5,3,.6,38,66),
    (6,0,2.25,33,82),(6,3,.75,33,70),
    (7,0,1.8,33,82),(7,2.75,.5,37,67),(7,3.5,.35,33,74),
]
bass=[(bar*4+beat,dur,pitch,vel) for bar,beat,dur,pitch,vel in bass_pattern]
chords=[
    [53,57,62,64],[53,57,62,64],
    [53,57,58,62],[53,57,58,62],
    [55,58,62,69],[55,58,62,69],
    [57,62,64,69],[57,61,64,69],
]
placements=[[(.5,1.75,57),(3.25,.5,48)],[(1,2,53)],
            [(.5,1.75,55),(3,.5,47)],[(.75,2.25,52)],
            [(.5,1.5,56),(3.25,.5,46)],[(1,2,51)],
            [(.5,2.5,54)],[(0,2,55),(3,.5,45)]]
keys=[]
for bar, (chord, hits) in enumerate(zip(chords,placements)):
    for beat,dur,vel in hits:
        for j,pitch in enumerate(chord):
            keys.append((bar*4+beat,dur,pitch,vel+[-3,1,-1,3][j]))
make(OUT/'KEYS_Dm_96bpm_8bars.mid','KEYS_TINES',keys)
make(OUT/'BASS_Dm_96bpm_8bars.mid','BASS_SUB',bass)

# Independent small SMF reader: verify emitted events, note lifetimes and duration.
def read_vlq(data,p):
    n=0
    for _ in range(4):
        b=data[p];p+=1;n=(n<<7)|(b&127)
        if b<128:return n,p
    raise ValueError('Invalid VLQ')

def verify(path,monophonic=False):
    data=path.read_bytes()
    assert data[:4]==b'MThd'
    size,fmt,ntracks,division=struct.unpack('>IHHH',data[4:14])
    assert size==6 and fmt==1 and ntracks==2 and division==PPQ
    p=14; noteons=0; seen=[]; ends=[]
    for track in range(ntracks):
        assert data[p:p+4]==b'MTrk'
        length=struct.unpack('>I',data[p+4:p+8])[0]
        block=data[p+8:p+8+length];p+=8+length
        j=0;t=0;active=set()
        while j<len(block):
            dt,j=read_vlq(block,j);t+=dt
            st=block[j];j+=1
            if st==255:
                typ=block[j];j+=1
                ln,j=read_vlq(block,j)
                payload=block[j:j+ln];j+=ln
                if typ==81:assert int.from_bytes(payload,'big')==TEMPO
                if typ==47:assert ln==0 and t==TOTAL
            else:
                assert st in (128,144)
                pitch,vel=block[j:j+2];j+=2
                if st==144:
                    assert pitch not in active
                    active.add(pitch);noteons+=1;seen.append(pitch)
                    if monophonic:assert len(active)==1
                else:
                    assert pitch in active
                    active.remove(pitch)
        assert not active
        ends.append(t)
    assert p==len(data) and all(x==TOTAL for x in ends)
    return {'file':path.name,'format':fmt,'ppq':division,'tracks':ntracks,'notes':noteons,'pitch_min':min(seen),'pitch_max':max(seen),'seconds':TOTAL/PPQ*TEMPO/1e6,'note_lifetimes_valid':True}

readme='''SUNO v6 / STUDIO 2.0 — УЧЕБНЫЕ MIDI-ОПОРЫ
11 сентября 2026

Два оригинальных учебных MIDI-файла для работы с нотами и Wavetable.
Это НЕ аудио Suno и НЕ результат тестовой генерации v6.

ПАРАМЕТРЫ
96 BPM; 4/4; D minor; 8 тактов; ровно 20 секунд.
SMF Type 1, 480 PPQ; conductor + note track.
KEYS: 48 нотных событий, редкие аккордовые атаки.
BASS: 17 нот, монофоническая партия, MIDI note numbers 31–45.
Нет Program Change: тембр нужно назначить самостоятельно.

ГАРМОНИЯ ПО ТАКТАМ
1–2: Dm(add9)
3–4: Bbmaj7
5–6: Gm(add9)
7: Asus4
8: A
C-sharp в последнем A и басовом подходе — осознанная доминанта к D minor.

КАК ИСПОЛЬЗОВАТЬ
1. Создай Studio-проект или его учебную копию; выставь 96 BPM и 4/4.
2. Импортируй каждый MIDI на отдельную MIDI-дорожку с одного общего старта.
3. Назначь KEYS синтетический клавишный патч, BASS — mono sine/sub-патч.
4. Если импорт не забирает tempo metadata, выставь 96 BPM вручную.
5. Проверь регистр: названия октав в разных DAW могут отличаться.
6. Начинай на умеренной громкости. Отредактируй ноты/velocity по вкусу.
7. Добавляй drums на пустую AUDIO-дорожку, выделив эти же восемь тактов.
8. Для ТОЧНЫХ нот оставь MIDI. MIDI-to-generated-audio — новая вероятностная
   интерпретация, не гарантированная точная смена тембра.

Wavetable — синтезатор, не сэмплированный акустический рояль. Для настоящего
piano library используй подходящий инструмент в своей внешней DAW.

Файлы проверены структурно, не прослушаны/не импортированы в твоём аккаунте
Suno. Звук и хвосты будут зависеть от выбранного инструмента и эффектов.
'''
reports=[verify(OUT/'KEYS_Dm_96bpm_8bars.mid'),verify(OUT/'BASS_Dm_96bpm_8bars.mid',True)]
readme=readme.replace('KEYS: 48 нотных событий',f"KEYS: {reports[0]['notes']} нотных событий")
(OUT/'README.txt').write_text(readme)
(ROOT/'_work'/'v6_midi_validation.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
zip_path=ROOT/'suno_v6_midi_starters_96bpm.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for file in sorted(OUT.iterdir()):
        z.write(file,file.name)
print(json.dumps(reports,ensure_ascii=False,indent=2))
print(zip_path.name,zip_path.stat().st_size,'bytes')
