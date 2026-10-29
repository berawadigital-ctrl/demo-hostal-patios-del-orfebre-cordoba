# Contenido de la demo Hostal Patios del Orfebre (Córdoba) (es/ca/en/fr). Hechos de patiosdelorfebre.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Junior Suite','Doble estándar','Triple'],'ca':['Junior Suite','Doble estàndard','Triple'],'en':['Junior Suite','Standard double','Triple'],'fr':['Junior Suite','Double standard','Triple']}
RD={
'es':['60 m² en lo más alto de la casa-patio: dormitorio con cama de matrimonio, salón con vistas a la Mezquita-Catedral y solárium privado.','12 m², cama doble o dos individuales, suelos porcelánicos y baño moderno con ducha.','16 m², tres camas individuales, frente al patio mayor con el yacimiento arqueológico del siglo IV.'],
'ca':['60 m² a la part més alta de la casa-pati: dormitori amb llit de matrimoni, saló amb vistes a la Mesquita-Catedral i solàrium privat.','12 m², llit doble o dos individuals, terres de porcellànic i bany modern amb dutxa.','16 m², tres llits individuals, davant del pati gran amb el jaciment arqueològic del segle IV.'],
'en':['60 m² at the top of the patio house: bedroom with a double bed, a lounge overlooking the Mosque-Cathedral and a private sun terrace.','12 m², double bed or two singles, porcelain floors and a modern bathroom with shower.','16 m², three single beds, facing the main patio with the 4th-century archaeological site.'],
'fr':['60 m² au plus haut de la maison à patio : chambre avec lit double, salon avec vue sur la Mosquée-Cathédrale et solarium privé.','12 m², lit double ou deux lits simples, sols en grès porcelaine et salle de bain moderne avec douche.','16 m², trois lits simples, face au grand patio avec le site archéologique du IVe siècle.']}
ART={
'hero':('arches',9301,['#f5ede1','#e5be8c','#b5602f','#5a3a24','#3b2617']),
'intro':('columns',9302,['#f2ece2','#faf6ef','#b8692f','#5a3a24','#3b2617']),
'r1':('arches',9311,['#f4ebde','#e2b986','#b05a2c','#5a3a24','#3b2617']),
'r2':('columns',9312,['#f0eadf','#f8f4ec','#b4652d','#5a3a24','#3b2617']),
'r3':('hills',9313,['#e9eef0','#f4ecd8','#eab878','#b4c49f','#89a286','#5d7a63']),
'g1':('arches',9321,['#f3e9dc','#dfb480','#ab562a','#5a3a24','#3b2617']),
'g2':('columns',9322,['#eee8dc','#f7f2ea','#b1622b','#5a3a24','#3b2617']),
'g3':('skyline',9323,['#5a3a24','#e8a964','#f7d8a5','#523521','#432b1b','#2e1d12']),
'g4':('arches',9324,['#f2e8da','#ddb07c','#a85328','#5a3a24','#3b2617']),
'g5':('hills',9325,['#e6ecee','#f1e9d2','#e7b474','#b0c09a','#86a083','#5a7660']),
'g6':('columns',9326,['#ede6da','#f6f1e8','#ae5f29','#5a3a24','#3b2617'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Patios del Orfebre · Casa-patio del siglo XVI en la judería de Córdoba',see_rooms='Ver habitaciones',hero_k='Córdoba · Centro histórico',hero_t='Una casa-patio del siglo XVI en el corazón de Córdoba',hero_s='A 180 m de la puerta de Almodóvar y a 450 m de la Mezquita-Catedral, entre las calles estrechas de la judería.',
 intro_t='Patios, historia y descanso',intro_p1='Las habitaciones se disponen alrededor de los patios aporticados de una casa restaurada que respeta todas sus partes originales.',
 intro_p2='En el patio mayor puede verse un yacimiento arqueológico hallado durante las obras, datado alrededor del siglo IV.',
 stats=['Siglo XVI','22 habitaciones','Wifi gratuito','Centro histórico'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='22 habitaciones, todas diferentes, de la individual a la Junior Suite.',
 svcs=['Wifi gratuito','Aire acondicionado con bomba de calor','Televisión','Minibar','Baño con ducha y secador','Cerradura electrónica de proximidad','Limpieza ecosostenible','Parking público a 150 m'],
 loc_p='Calle Tejón y Marín 1 · 14003 Córdoba. Hostal 1* · RTA H/CO/00814.',
 chips=['¿Qué habitaciones tiene?','¿Dónde está?','¿A qué hora es el check-in?','¿Cómo se reserva?']),
'ca':dict(title='Hostal Patios del Orfebre · Casa-pati del segle XVI al call de Còrdova',see_rooms='Veure habitacions',hero_k='Còrdova · Centre històric',hero_t='Una casa-pati del segle XVI al cor de Còrdova',hero_s='A 180 m de la porta d\'Almodóvar i a 450 m de la Mesquita-Catedral, entre els carrers estrets del call.',
 intro_t='Patis, història i descans',intro_p1='Les habitacions s\'organitzen al voltant dels patis porticats d\'una casa restaurada que respecta totes les parts originals.',
 intro_p2='Al pati gran es pot veure un jaciment arqueològic trobat durant les obres, datat al voltant del segle IV.',
 stats=['Segle XVI','22 habitacions','Wifi gratuït','Centre històric'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='22 habitacions, totes diferents, de la individual a la Junior Suite.',
 svcs=['Wifi gratuït','Aire condicionat amb bomba de calor','Televisió','Minibar','Bany amb dutxa i assecador','Pany electrònic de proximitat','Neteja ecosostenible','Pàrquing públic a 150 m'],
 loc_p='Calle Tejón y Marín 1 · 14003 Còrdova. Hostal 1* · RTA H/CO/00814.',
 chips=['Quines habitacions té?','On és?','A quina hora és el check-in?','Com es reserva?']),
'en':dict(title='Hostal Patios del Orfebre · 16th-century patio house in Córdoba\'s Jewish quarter',see_rooms='See the rooms',hero_k='Córdoba · Historic centre',hero_t='A 16th-century patio house in the heart of Córdoba',hero_s='180 m from the Almodóvar gate and 450 m from the Mosque-Cathedral, among the narrow streets of the Jewish quarter.',
 intro_t='Patios, history and rest',intro_p1='The rooms are set around the arcaded patios of a restored house that keeps all its original parts.',
 intro_p2='In the main patio you can see an archaeological site found during the works, dated to around the 4th century.',
 stats=['16th century','22 rooms','Free wifi','Historic centre'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='22 rooms, all different, from the single to the Junior Suite.',
 svcs=['Free wifi','Heat-pump air conditioning','TV','Minibar','Bathroom with shower and hairdryer','Electronic proximity lock','Eco-friendly cleaning','Public car park 150 m away'],
 loc_p='Calle Tejón y Marín 1 · 14003 Córdoba. 1-star hostal · RTA H/CO/00814.',
 chips=['What rooms does it have?','Where is it?','What time is check-in?','How do I book?']),
'fr':dict(title='Hostal Patios del Orfebre · Maison à patio du XVIe siècle dans la juiverie de Cordoue',see_rooms='Voir les chambres',hero_k='Cordoue · Centre historique',hero_t='Une maison à patio du XVIe siècle au cœur de Cordoue',hero_s='À 180 m de la porte d\'Almodóvar et à 450 m de la Mosquée-Cathédrale, dans les ruelles de la juiverie.',
 intro_t='Patios, histoire et repos',intro_p1='Les chambres s\'organisent autour des patios à arcades d\'une maison restaurée qui conserve toutes ses parties d\'origine.',
 intro_p2='Dans le grand patio, on peut voir un site archéologique découvert pendant les travaux, daté du IVe siècle environ.',
 stats=['XVIe siècle','22 chambres','Wifi gratuit','Centre historique'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='22 chambres, toutes différentes, de l\'individuelle à la Junior Suite.',
 svcs=['Wifi gratuit','Climatisation par pompe à chaleur','Télévision','Minibar','Salle de bain avec douche et sèche-cheveux','Serrure électronique de proximité','Nettoyage écoresponsable','Parking public à 150 m'],
 loc_p='Calle Tejón y Marín 1 · 14003 Cordoue. Hostal 1* · RTA H/CO/00814.',
 chips=['Quelles chambres a-t-il ?','Où est-il ?','À quelle heure est le check-in ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='reservas@patiosdelorfebre.es')
D=dict(name='Hostal Patios del Orfebre',ac='#5a3a24',ac2='#b5602f',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='Calle Tejón y Marín 1 · 14003 Córdoba',phones=['+34 957 392 975'],emails=['reservas@patiosdelorfebre.es'],maps='Hostal Patios del Orfebre, Calle Tejón y Marín 1, Córdoba',t=T)
META=dict(repo='demo-hostal-patios-del-orfebre-cordoba',name='Hostal Patios del Orfebre',legal_name='Orfebre Management 1877, S.L.',registry_ids=['CIF B-67863910','RTA H/CO/00814'],
 url='https://patiosdelorfebre.es/',domain='patiosdelorfebre.es',municipality='Córdoba',province='Córdoba',sector='hostal de 1 estrella en una casa-patio del siglo XVI del centro histórico de Córdoba',
 read_at='2026-10-29T13:10:00+01:00',created_at='2026-10-29T13:09:00+01:00',built_at='2026-10-29T13:25:00+01:00',audit_date='2026-10-29T13:02:20+01:00',
 rating=dict(value=4.7,coincide=['telefono','web'],date='2026-10-29T11:06:28+01:00',url='https://www.google.com/maps/place/Hostal+Patios+del+Orfebre/@37.8819896,-4.7842755,17z/data=!4m9!3m8!1s0xd6cdf62045f6cbf:0xddaad35cdeb240c4!5m2!4m1!1i2!8m2!3d37.8819896!4d-4.7842755!16s%2Fg%2F11hcxhq22z'),
 book=dict(mode='mail',url='mailto:reservas@patiosdelorfebre.es',note='Su web no ofrece un motor de reservas enlazable (el plugin de reservas muestra precios vacíos y no tiene pagina de reserva publica); la reserva se pide por correo a reservas@patiosdelorfebre.es, el canal que la propia web indica. La demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Cómo es la Junior Suite?','K02'),('¿Dónde está?','K03'),('¿A qué hora es el check-in?','K04'),('¿Hay recepción 24 horas?','K05'),('¿Puedo cancelar gratis?','K06'),('¿Hay aparcamiento cerca?','K07'),('¿Qué tienen las habitaciones?','K08'),('¿Qué historia tiene la casa?','K09'),('¿Cómo reservo?','K10'),('¿Quién es el titular?','K11'),('¿Se puede fumar?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Com és la Junior Suite?','K02'),('On és?','K03'),('A quina hora és el check-in?','K04'),('Hi ha recepció 24 hores?','K05'),('Puc cancel·lar gratis?','K06'),('Hi ha aparcament a prop?','K07'),('Què tenen les habitacions?','K08'),('Quina història té la casa?','K09'),('Com reservo?','K10'),('Qui és el titular?','K11'),('Es pot fumar?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What is the Junior Suite like?','K02'),('Where is it?','K03'),('What time is check-in?','K04'),('Is there a 24-hour reception?','K05'),('Can I cancel for free?','K06'),('Is there parking nearby?','K07'),('What do the rooms have?','K08'),('What is the history of the house?','K09'),('How do I book?','K10'),('Who is the owner?','K11'),('Can I smoke?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Comment est la Junior Suite ?','K02'),('Où est-il ?','K03'),('À quelle heure est le check-in ?','K04'),('Y a-t-il une réception 24 heures ?','K05'),('Puis-je annuler gratuitement ?','K06'),('Y a-t-il un parking à proximité ?','K07'),('Qu\'ont les chambres ?','K08'),('Quelle est l\'histoire de la maison ?','K09'),('Comment réserver ?','K10'),('Qui est le titulaire ?','K11'),('Peut-on fumer ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
