from pathlib import Path
import math
P=Path(__file__).parent/'assets';P.mkdir(parents=True,exist_ok=True)

def svg(shape,accent='#d9a98b',bg='#f2ede7',size=700):
    a=accent
    head='''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="700" viewBox="0 0 700 700"><defs>
    <radialGradient id="bg" cx="48%" cy="36%" r="75%"><stop stop-color="#ffffff" stop-opacity=".72"/><stop offset="1" stop-color="'''+bg+'''" stop-opacity="1"/></radialGradient>
    <linearGradient id="shine" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#ffffff" stop-opacity=".75"/><stop offset=".45" stop-color="#ffffff" stop-opacity=".05"/><stop offset="1" stop-color="#000000" stop-opacity=".13"/></linearGradient>
    <linearGradient id="metal" x1="0" x2="1"><stop stop-color="#5f6569"/><stop offset=".24" stop-color="#f4f4f0"/><stop offset=".54" stop-color="#aaaeb1"/><stop offset=".78" stop-color="#f7f7f7"/><stop offset="1" stop-color="#50555a"/></linearGradient>
    <linearGradient id="dark" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#54585a"/><stop offset="1" stop-color="#15191b"/></linearGradient>
    <filter id="shadow"><feGaussianBlur stdDeviation="18"/></filter>
    <pattern id="mesh" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="5" cy="5" r="1.3" fill="#eee" opacity=".4"/></pattern>
    </defs><rect width="700" height="700" fill="url(#bg)"/>
    <circle cx="555" cy="143" r="170" fill="'''+a+'''" opacity=".095"/>
    <ellipse cx="356" cy="576" rx="190" ry="29" fill="#222" opacity=".16" filter="url(#shadow)"/>'''
    return head+shape+'</svg>'

def img(name,inner,accent,bg):
    (P/(name+'.svg')).write_text(svg(inner,accent,bg),encoding='utf-8')

# all illustrations are original vector assets generated for this project
headphones='''<g transform="translate(0 5)"><path d="M220 368V303C220 168 480 168 480 303v65" fill="none" stroke="#25272a" stroke-width="57" stroke-linecap="round"/><path d="M222 337v-41c0-155 257-155 257 0v41" fill="none" stroke="url(#metal)" stroke-width="15"/><rect x="171" y="339" width="100" height="180" rx="46" fill="#222528"/><rect x="429" y="339" width="100" height="180" rx="46" fill="#222528"/><rect x="181" y="348" width="69" height="160" rx="34" fill="url(#dark)"/><rect x="450" y="348" width="69" height="160" rx="34" fill="url(#dark)"/><path d="M183 378q18-24 37-22" stroke="#fff" stroke-opacity=".36" stroke-width="9" fill="none"/><path d="M452 378q18-24 37-22" stroke="#fff" stroke-opacity=".28" stroke-width="8" fill="none"/><circle cx="222" cy="477" r="4" fill="#e1b991"/></g>'''
img('headphones',headphones,'#d0b7a2','#eeece8')
headphones2=headphones.replace('#222528','#d8c6b7').replace('#222528','#d8c6b7').replace('#222528','#d8c6b7').replace('#222528','#d8c6b7').replace('#25272a','#9e8978').replace('#222528','#dcc7b6').replace('url(#dark)','#cab4a5')
img('headphones-sand',headphones2,'#e4c2a6','#efe9e1')
speaker='''<g><rect x="220" y="224" width="260" height="304" rx="65" fill="#292c2d"/><rect x="234" y="234" width="232" height="280" rx="57" fill="url(#mesh)"/><rect x="250" y="250" width="200" height="253" rx="49" fill="#292c2d" opacity=".45"/><rect x="284" y="244" width="132" height="7" rx="3" fill="#fff" opacity=".3"/><circle cx="350" cy="455" r="9" fill="#c8aa91"/><path d="M284 308c24-28 108-29 133 0" fill="none" stroke="#fff" opacity=".09" stroke-width="12"/></g>'''
img('speaker',speaker,'#b6b3b3','#e9e5e0')
img('speaker-cream',speaker.replace('#292c2d','#afa397').replace('#c8aa91','#3d322b'),'#d0bca6','#f2eae0')
lamp='''<g><path d="M310 195l-82 152q122 34 244 0l-82-152z" fill="#c2b6a8"/><path d="M310 195l-82 152q122 34 244 0l-82-152z" fill="url(#shine)"/><ellipse cx="350" cy="348" rx="121" ry="22" fill="#6f675e"/><ellipse cx="350" cy="345" rx="109" ry="16" fill="#f3dfbd"/><rect x="338" y="365" width="24" height="164" rx="9" fill="url(#metal)"/><ellipse cx="350" cy="537" rx="121" ry="18" fill="#73736e"/><ellipse cx="350" cy="532" rx="121" ry="17" fill="url(#metal)"/><ellipse cx="350" cy="531" rx="75" ry="7" fill="#ccc9c2"/></g>'''
img('lamp',lamp,'#d7bd98','#efeae1')
img('lamp-black',lamp.replace('#c2b6a8','#383a39').replace('#6f675e','#1d2020').replace('#f3dfbd','#cfbc9b'),'#8a918d','#e7e9e5')
watch='''<g transform="rotate(-13 350 350)"><rect x="300" y="105" width="100" height="504" rx="35" fill="#d4c6b2"/><path d="M313 129h74v130h-74zM313 445h74v133h-74z" fill="#beaa94" opacity=".5"/><rect x="262" y="248" width="176" height="217" rx="51" fill="#656866"/><rect x="271" y="258" width="158" height="199" rx="43" fill="url(#dark)"/><rect x="285" y="271" width="131" height="173" rx="31" fill="#101719"/><path d="M350 308v60l39 28" stroke="#efe7d6" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="350" cy="368" r="7" fill="#d9b991"/><circle cx="350" cy="368" r="55" stroke="#e3dfd4" stroke-width="2" opacity=".3" fill="none"/><rect x="437" y="329" width="13" height="32" rx="6" fill="#d3b99d"/></g>'''
img('watch',watch,'#e0d3b5','#e9e8e1')
shoe='''<g transform="translate(-6 19)"><path d="M129 422q42 12 99-36l54-82q18-27 55-8l92 85 91 41q52 13 65 65l-4 22q-7 25-41 26H165q-49 0-55-31z" fill="#d4c4aa"/><path d="M139 421q58 8 111-40l44-62 120 96q54 37 111 32" fill="none" stroke="#f8f1e5" stroke-width="17"/><path d="M110 497q127 11 249 7t225-14q3 46-40 49H159q-48 0-49-42z" fill="#f8f8f4"/><path d="M122 509q220 32 448-5" fill="none" stroke="#c5bbb0" stroke-width="7"/><path d="M281 348l91 45m-112-19 89 46m-117-16 86 44" stroke="#6c6a66" stroke-width="9" stroke-linecap="round"/><path d="M445 396q47 16 74 41" stroke="#a59b89" stroke-width="13" fill="none"/><path d="M145 441l-7 35" stroke="#988b76" stroke-width="18"/></g>'''
img('sneaker',shoe,'#d6bba1','#ece8e3')
img('sneaker-dark',shoe.replace('#d4c4aa','#4d5b59').replace('#f8f1e5','#9eafa7'),'#99aaa0','#e6e8e4')
backpack='''<g><path d="M265 248v-33q0-72 85-72t85 72v33" fill="none" stroke="#75766d" stroke-width="21"/><path d="M251 250q-35 0-39 65l-18 205q-2 37 38 42h236q41-4 39-42l-18-205q-6-65-42-65z" fill="#8e9b86"/><path d="M251 250q-35 0-39 65l-18 205q-2 37 38 42h236q41-4 39-42l-18-205q-6-65-42-65z" fill="url(#shine)"/><rect x="268" y="213" width="165" height="43" rx="21" fill="#7e8c78"/><rect x="245" y="365" width="210" height="155" rx="26" fill="#829078" stroke="#667262" stroke-width="4"/><path d="M253 397h193" stroke="#d4dec8" stroke-width="9" opacity=".7"/><rect x="326" y="383" width="48" height="29" rx="8" fill="#bbbaac"/><path d="M236 320v174M463 320v174" stroke="#485a4e" opacity=".5" stroke-width="11"/></g>'''
img('backpack',backpack,'#a8bb9f','#e8eae4')
img('backpack-black',backpack.replace('#8e9b86','#42484a').replace('#829078','#353e40').replace('#7e8c78','#404849').replace('#667262','#303638').replace('#d4dec8','#afb8b8'),'#9ca5a5','#ecebea')
sunglasses='''<g transform="rotate(-7 350 350)"><path d="M121 316q-13-32 27-35h105q54 1 89 33l13 7 13-7q37-32 90-33h99q42 1 27 35l-39 108q-11 26-45 26H430q-38 0-55-37l-18-53q-4-13-13-13t-14 13l-17 53q-17 37-55 37h-76q-34 0-45-26z" fill="#292d2d"/><path d="M144 318h111q43 4 68 32l-21 62q-11 23-34 23h-76q-26 0-32-21zM455 318h104l-16 96q-6 21-32 21h-76q-23 0-34-23l-21-62q32-32 75-32z" fill="#676963"/><path d="M160 326q28 3 48 19m248-19q27 4 52 19" stroke="#fff" opacity=".34" stroke-width="12" stroke-linecap="round"/><path d="M122 301 68 281m510 20 54-20" stroke="#313435" stroke-width="16" stroke-linecap="round"/></g>'''
img('sunglasses',sunglasses,'#adad9d','#eae9e3')
bottle='''<g><rect x="306" y="142" width="88" height="53" rx="11" fill="#525d58"/><rect x="292" y="180" width="116" height="56" rx="18" fill="#7e8981"/><path d="M269 249q0-39 34-43h94q34 4 34 43v258q0 43-39 43h-84q-39 0-39-43z" fill="#bfc9c1"/><path d="M269 249q0-39 34-43h94q34 4 34 43v258q0 43-39 43h-84q-39 0-39-43z" fill="url(#shine)"/><rect x="303" y="295" width="8" height="167" rx="4" fill="#fff" opacity=".3"/><text x="350" y="413" fill="#3f5549" font-family="Arial" font-size="19" letter-spacing="7" text-anchor="middle">FORM</text></g>'''
img('bottle',bottle,'#b7c6ba','#e9ede7')
img('bottle-rose',bottle.replace('#bfc9c1','#cfa49d').replace('#525d58','#775a54').replace('#7e8981','#ad7974'),'#e1b5b0','#f0e8e4')
mug='''<g><path d="M237 255h219v217q0 65-100 72t-119-72z" fill="#e1d6c5"/><path d="M237 255h219v217q0 65-100 72t-119-72z" fill="url(#shine)"/><path d="M459 297q99-19 95 75t-97 83" fill="none" stroke="#c0ae99" stroke-width="37"/><path d="M459 310q77-12 72 62t-72 66" fill="none" stroke="#efe5d8" stroke-width="15"/><ellipse cx="346" cy="254" rx="111" ry="21" fill="#b1a595"/><ellipse cx="346" cy="253" rx="98" ry="12" fill="#755843"/><ellipse cx="346" cy="248" rx="94" ry="8" fill="#99725a"/><path d="M280 330v122" stroke="#fff" opacity=".38" stroke-width="11" stroke-linecap="round"/></g>'''
img('mug',mug,'#d2bda9','#eee8df')
earbuds='''<g><rect x="216" y="321" width="268" height="180" rx="76" fill="#eeeae3" stroke="#c5c3bc" stroke-width="5"/><path d="M222 381h257" stroke="#b4b4af" stroke-width="5"/><circle cx="350" cy="438" r="6" fill="#d2b5a0"/><g fill="#f1ece8" stroke="#b7b7b3" stroke-width="4"><path d="M275 200q-22 6-23 42 1 36 34 40v98q0 25 20 24t19-24V244q0-44-50-44z"/><path d="M425 200q22 6 23 42-1 36-34 40v98q0 25-20 24t-19-24V244q0-44 50-44z"/></g><path d="M270 220q14-16 30 0m130 0q-14-16-30 0" fill="none" stroke="#fff" stroke-width="9" opacity=".9"/></g>'''
img('earbuds',earbuds,'#d6c4b2','#ebe9e7')
chair='''<g><path d="M224 192q18-56 83-55h100q68 0 80 55l27 165q4 45-46 56H239q-50-10-46-56z" fill="#9c8573"/><path d="M239 227q10-49 77-50h92q47 0 58 50l21 138q1 29-38 35H249q-36-7-35-35z" fill="#b8a28b"/><path d="M214 398q-19 0-27 28t27 36h278q45 0 31-36-9-27-32-28z" fill="#937c6b"/><path d="M252 463l-24 110m222-110 28 110" stroke="#484643" stroke-width="17" stroke-linecap="round"/><path d="M240 463h223" stroke="#625b52" stroke-width="17"/><path d="M246 241q0-34 33-38" stroke="#fff" stroke-width="9" opacity=".12" fill="none"/></g>'''
img('chair',chair,'#d9bda0','#e9e3da')
tote='''<g><path d="M273 261v-36q0-76 77-76t77 76v36" fill="none" stroke="#9f8267" stroke-width="19"/><path d="M235 251h230l38 281q3 28-30 29H227q-33-1-30-29z" fill="#d2bc9f"/><path d="M235 251h230l38 281q3 28-30 29H227q-33-1-30-29z" fill="url(#shine)"/><path d="M269 263V223q0-81 81-81t81 81v40" fill="none" stroke="#bd9c78" stroke-width="19"/><text x="350" y="412" font-family="Georgia" text-anchor="middle" font-size="57" letter-spacing="-4" fill="#77644e">F.</text><path d="M227 540h244" stroke="#b8a084" stroke-width="5"/></g>'''
img('tote',tote,'#dbbf9c','#eeeae2')
keyboard='''<g transform="rotate(-10 350 350)"><rect x="125" y="294" width="450" height="208" rx="22" fill="#777771"/><rect x="137" y="297" width="427" height="185" rx="16" fill="#b3b2ab"/>'''
for row,(y,n) in enumerate([(318,12),(359,12),(400,11),(441,8)]):
    for i in range(n):
        x=151+i*(33 if row<3 else 39)
        w=29 if row<3 else 34
        if row==3 and i==3:w=126
        if row==3 and i>3:x+=92
        keyboard+=f'<rect x="{x}" y="{y}" width="{w}" height="29" rx="5" fill="{["#f0ede5","#e6e1d8","#d5a88a"][((i*7+row*3)%17)//7]}" stroke="#999993" stroke-width="1"/>'
keyboard+='</g>'
img('keyboard',keyboard,'#bcb9b0','#e9e8e3')
diffuser='''<g><rect x="302" y="133" width="96" height="55" rx="8" fill="#b5aa97"/><rect x="276" y="180" width="148" height="320" rx="25" fill="#ded0b7"/><rect x="276" y="180" width="148" height="320" rx="25" fill="url(#shine)"/><rect x="299" y="208" width="102" height="263" rx="13" fill="#f4ece0" opacity=".16"/><path d="M351 182 266 78m83 104 1-126m1 126 88-105m-88 105 48-139m-48 139-56-135" stroke="#9e7c5e" stroke-width="9" stroke-linecap="round"/><text x="350" y="392" font-family="Georgia" font-size="24" text-anchor="middle" fill="#827363">atelier</text><path d="M319 413h62" stroke="#aaa18e" stroke-width="2"/></g>'''
img('diffuser',diffuser,'#d2c4b1','#f1eae1')
camera='''<g><rect x="195" y="287" width="309" height="203" rx="27" fill="#33393a"/><rect x="240" y="258" width="116" height="40" rx="11" fill="#33393a"/><rect x="407" y="269" width="60" height="22" rx="9" fill="#5e6868"/><rect x="205" y="302" width="288" height="172" rx="20" fill="url(#dark)"/><circle cx="350" cy="388" r="93" fill="#171b1d" stroke="#999c98" stroke-width="12"/><circle cx="350" cy="388" r="76" fill="#222a2b" stroke="#727e80" stroke-width="9"/><circle cx="350" cy="388" r="57" fill="#15262c" stroke="#536971" stroke-width="5"/><circle cx="350" cy="388" r="35" fill="#203c47"/><circle cx="335" cy="370" r="14" fill="#99b7bb" opacity=".55"/><circle cx="467" cy="322" r="11" fill="#dfba91"/></g>'''
img('camera',camera,'#abaeae','#e8e8e6')
mouse='''<g transform="rotate(18 350 350)"><path d="M350 181q-111 0-130 136l-1 108q5 129 131 129t131-129V317Q460 181 350 181z" fill="#c9c6c0"/><path d="M350 181q-111 0-130 136l-1 108q5 129 131 129t131-129V317Q460 181 350 181z" fill="url(#shine)"/><path d="M350 186v140" stroke="#8f8e8a" stroke-width="4"/><rect x="341" y="268" width="18" height="52" rx="9" fill="#6f716e"/><path d="M222 364h258" stroke="#c2c1b9" stroke-width="3"/></g>'''
img('mouse',mouse,'#dedbd5','#ebebe8')
clock='''<g><circle cx="350" cy="355" r="190" fill="#c7b59d"/><circle cx="350" cy="355" r="174" fill="#f5eee2"/><circle cx="350" cy="355" r="159" fill="#eae2d5"/>'''
for i in range(12):
    theta=math.pi*(i/6)-math.pi/2
    x1=350+142*math.cos(theta);y1=355+142*math.sin(theta)
    x2=350+152*math.cos(theta);y2=355+152*math.sin(theta)
    clock+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#8a8074" stroke-width="4" stroke-linecap="round"/>'
clock+='''<path d="M350 249v111l85 46" stroke="#55514d" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="350" cy="355" r="10" fill="#d3a784"/><text x="350" y="445" text-anchor="middle" font-family="Georgia" font-size="15" letter-spacing="5" fill="#938b7d">FORMA</text></g>'''
img('clock',clock,'#d5c8b4','#eeeae3')
stand='''<g><path d="M253 457l176-266q17-28 42-13l14 8q21 13 4 39L311 488" fill="#9a9b96"/><path d="M266 451l176-266" stroke="#eee" stroke-width="12" opacity=".6"/><path d="M225 476h249q35 0 35 32t-35 32H225q-35 0-35-32t35-32z" fill="#bfc0b8"/><path d="M224 484h248" stroke="#fff" opacity=".55" stroke-width="8"/><rect x="268" y="164" width="204" height="282" rx="24" fill="#303b3c" transform="rotate(-18 370 305)"/><rect x="280" y="176" width="180" height="257" rx="17" fill="#a6b8b1" transform="rotate(-18 370 305)"/><circle cx="394" cy="201" r="4" fill="#293d40"/></g>'''
img('stand',stand,'#b0bcb6','#e6eae7')
print('Created',len(list(P.glob('*.svg'))),'SVG illustration assets')
