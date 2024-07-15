import discord ,random ,requests,os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado secion como EcoloyicBot {bot.user}')
    

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
 

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def ayuda(ctx):
    await ctx.send("!Ecologia1 - Te da la bienvenida al ecologia y te la explica")
    await ctx.send("!Ecologia2 - Te explica los factores bióticos y abióticos")
    await ctx.send("!escalaspart1 - Te explica los niveles de la ecologia")
    await ctx.send("!escalaspart2 - es la continuacion de !escalaspart1")
    await ctx.send("!escalaspart3 - es la continuacion de !escalaspart2")
    await ctx.send("!animales - te da una breve explicacion sobre los factores bióticos y abióticos en animales")
    await ctx.send("!manualidades - te da los comandos para distintos tipos de manualidades")
@bot.command()
async def Ecologia1(ctx):
    await ctx.send("¡Bienvenido a la ecología!"
                    "¿Alguna vez has paseado por el bosque y has visto la increíble diversidad de organismos que viven juntos, de los helechos a los árboles, a los hongos del tamaño de platos? ¿O has viajado por carretera y visto por la ventana cómo va cambiando el paisaje, de los bosques de encinos a los pinos altos, a los pastizales? Si es así, ya conoces lo más clásico de la ecología, la rama de la biología que estudia cómo los organismos interactúan entre ellos y con su entorno físico."
                    "Sin embargo, la ecología no se trata solo de bosques ricos en especies, naturaleza virgen o vistas panorámicas. ¿Alguna vez has encontrado cucarachas viviendo bajo tu cama, moho creciendo en tu ducha o incluso hongos invadiendo la piel entre tus dedos? Si es así, entonces has visto ejemplos igualmente válidos de la ecología en acción."
                    "Imágenes que ilustran las interacciones entre organismos y entre estos y su entorno físico."
                    "   Primera: hongos en un tronco con musgo."
                    "   Segunda: colinas verdes cubiertas de flores silvestres, pastos y algunos árboles."
                    "   Tercera: campos de pastos secos y amarillos, con colinas cubiertas de matorrales y montañas nevadas en la distancia."
                    "   Cuarta: cucarachas en el piso.")
    with open(f'imagenes1/img1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def Ecologia2(ctx):
    await ctx.send("Factores bióticos y abióticos---"
                    "Uno de los objetivos principales de la ecología es entender la distribución y abundancia de los seres vivos en el ambiente físico. Por ejemplo, tu jardín o el parque de tu barrio probablemente tiene un conjunto muy diferente de plantas, animales y hongos que el jardín de un compañero estudiante de Khan Academy al otro lado del mundo. Estos patrones en la naturaleza se basan en las interacciones entre los organismos y entre estos y su entorno físico."
                    "Como ejemplo, volvamos al moho de la ducha. Es más probable que el moho aparezca en tu ducha que, digamos, en el cajón de tus calcetines. ¿Por qué pasa esto?"
                    "Tal vez el moho requiere cierta cantidad de agua para crecer y esta cantidad de agua solo se puede encontrar en la ducha. La disponibilidad de agua es un ejemplo de un factor abiótico, o inerte, que puede afectar la distribución de los organismos."
                    "Tal vez el moho se alimenta de células cutáneas muertas que pueden encontrarse en la ducha pero no en el cajón. La disponibilidad de nutrientes proporcionada por otros organismos es un ejemplo de factor biótico, relacionado con los seres vivos, que puede influir en la distribución.")
@bot.command()
async def escalaspart1(ctx):
    await ctx.send("La ecología en muchas escalas-----"
                    "Dentro de la disciplina de la ecología, los investigadores trabajan en cinco amplios niveles, algunas veces por separado y en otras con superposición entre ellos: organismo, población, comunidad, ecosistema y biósfera."
                    "Demos un vistazo a cada nivel."
                    "Organismo: los ecólogos de organismos estudian las adaptaciones, las características benéficas que surgen por selección natural y que les permiten vivir en hábitats específicos. Estas adaptaciones pueden ser morfológicas, fisiológicas o conductuales."
                    "Población: una población es un grupo de organismos de la misma especie que vive en la misma área al mismo tiempo. Los ecólogos de poblaciones estudian el tamaño, la densidad y la estructura de las poblaciones y cómo cambian con el tiempo."
                    "Comunidad: una comunidad biológica se compone de todas las poblaciones de las diferentes especies que viven en un área determinada. Los ecólogos de comunidades se enfocan en las interacciones entre las poblaciones y cómo dichas interacciones le dan forma a la comunidad."
                    "Ecosistema: un ecosistema consiste de todos los organismos en un área, la comunidad, y los factores abióticos que influyen en esa comunidad. A menudo los ecólogos de ecosistemas se enfocan en el flujo de energía y el reciclaje de nutrientes."
                    "Biósfera: la biósfera es el planeta Tierra, visto como un sistema ecológico. Los ecólogos que trabajan a nivel de la biósfera pueden estudiar patrones globales —como el clima o la distribución de las especies—, interacciones entre ecosistemas y fenómenos que afectan a todo el planeta, como el cambio climático.")
@bot.command()
async def escalaspart2(ctx):
    await ctx.send("Un diagrama de flujo de tres cuadros que explica la jerarquía de los seres vivos."
                    "   El cuadro superior muestra una fotografía de árboles altos en un bosque y se titula" "Organismos, poblaciones y comunidades: en este bosque, cada pino es un organismo. Todos los pinos que viven en el área forman una población. Todas las poblaciones de las distintas especies que habitan el área forman una comunidad.   "
                    "   El segundo cuadro muestra una fotografía de un cuerpo de agua, detrás del cual hay pastos altos que se convierten en vegetación más densa a medida que la vista se aleja del agua, y hay algunos árboles al fondo. La foto esta acompañada del siguiente texto: ""Ecosistemas: este ecosistema costero en el sureste de los Estados Unidos consiste de una comunidad de organismos y su entorno físico.")
    with open(f'imagenes1/imgen2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def escalaspart3(ctx):
    await ctx.send( "El tercer cuadro muestra un dibujo del planeta Tierra y tiene una etiqueta que dice: ""La biósfera: la biósfera está compuesta de todos los ecosistemas de la Tierra, considerados como un conjunto.    "
                    "Un diagrama de flujo de tres cuadros que explica la jerarquía de los seres vivos."
                    "El cuadro superior muestra una fotografía de árboles altos en un bosque y se titula ""Organismos, poblaciones y comunidades: en este bosque, cada pino es un organismo. Todos los pinos que viven en el área forman una población. Todas las poblaciones de las distintas especies que habitan el área forman una comunidad."
                    "El segundo cuadro muestra una fotografía de un cuerpo de agua, detrás del cual hay pastos altos que se convierten en vegetación más densa a medida que la vista se aleja del agua, y hay algunos árboles al fondo. La foto esta acompañada del siguiente texto:" "Ecosistemas: este ecosistema costero en el sureste de los Estados Unidos consiste de una comunidad de organismos y su entorno físico."
                    "Los cinco niveles de la ecología se listan arriba del más pequeño al más grande. Se construyen de manera progresiva: las poblaciones se componen de individuos, las comunidades de poblaciones y los ecosistemas de comunidades más su entorno físico, y así sucesivamente. Cada nivel de organización tiene propiedades emergentes, propiedades nuevas que no existen en las partes que componen un nivel sino que surgen a partir de las interacciones y relaciones entre estas partes."
                    "Los niveles de estudio ecológico ofrecen diferentes perspectivas de las interacciones entre los organismos y de estos con su entorno. Me gusta pensar en estos niveles como lentes de aumento de diferentes potencias. Si realmente quieres saber qué es lo que sucede en un sistema ecológico en particular, ¡querrás usar más de uno!")

@bot.command()
async def animales1(ctx):
    await ctx.send("Estudio de caso: el panda rojo--"
                    "Usemos la idea de los factores bióticos y abióticos con otro organismo, uno que un ecólogo de campo podría estudiar. Los pandas rojos son parientes lejanos de los mapaches y solo se encuentran en los Himalayas orientales. Pasan la mayor parte del tiempo en los árboles y consumen una dieta principalmente vegetariana. En años recientes, la población de pandas rojos ha disminuido significativamente, lo que ha provocado que los grupos conservacionistas lo clasifiquen como una especie vulnerable o en peligro"
                    "¿Cuáles son los factores principales detrás de este cambio en la abundancia? Los ecólogos encontraron que los factores bióticos, como la tala de árboles y la introducción de enfermedades transmitidas por los perros domésticos, jugaron un papel fundamental en la disminución de las poblaciones de panda rojo."
                    "Los factores abióticos han sido menos importantes hasta el momento, pero el cambio en las temperaturas puede producir una mayor pérdida de su hábitat en el futuro."
                    "Entender los principales factores responsables de la disminución en la cantidad de pandas rojos ayuda a los ecólogos a crear planes de conservación para proteger a la especie.")
    with open(f'imagenes1/imgen1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def manualidades(ctx):
    await ctx.send("Tengo mas de 200 manualidades y cada vez que escojas una opcion de las de abajo te saldra una alazar")
    await ctx.send("!latas -- "
                    "!botellas -- "
                    "!cajas_de_carton")
@bot.command()
async def latas(ctx):
    await ctx.send (random.choice(["https://www.youtube.com/watch?v=N0ehRJ20_sE",
    "https://www.youtube.com/watch?v=Gabhl0MtHmM",
    "https://www.youtube.com/watch?v=i7Zqtawt4oY",
    "https://www.youtube.com/watch?v=UF5aoAfIYy4",
    "https://www.youtube.com/watch?v=_FnzsjKxYwU",
    "https://www.youtube.com/watch?v=us_YZbjrS6I",
    "https://www.youtube.com/watch?v=UfnC_YlD_AE",
    "https://www.youtube.com/watch?v=leDB-AiqLS0",
    "https://www.youtube.com/watch?v=3Du627dkm7k",
    "https://www.youtube.com/watch?v=zeIbKulYouU",
    "https://www.youtube.com/watch?v=l05C3VcUPUU"]))
    
@bot.command()
async def botellas(ctx):
    await ctx.send (random.choice(["https://www.youtube.com/watch?v=bSCcyH0iXGE",
    "https://www.youtube.com/watch?v=Xs2hAWuPmSg",
    "https://www.youtube.com/watch?v=FwEGLu3ssiU",
    "https://www.youtube.com/watch?v=wgVhEcMkCiY",
    "https://www.youtube.com/watch?v=pTDDrm3iYTo",
    "https://www.youtube.com/watch?v=YwHi8p-cQwk",
    "https://www.youtube.com/watch?v=xEAOvFG1AmM",
    "https://www.youtube.com/watch?v=2_gSe4VdThg",
    "https://www.youtube.com/watch?v=xCaI-5WVRlY",
    "https://www.youtube.com/watch?v=KZo3KR9wVL4",
    "https://www.youtube.com/watch?v=9RztExfFeo8",
    "https://www.youtube.com/watch?v=3EtyOm775Jo",
    "https://www.youtube.com/watch?v=KwjI0iDT4dw",
    "https://www.youtube.com/watch?v=BMOy_H7QklA",]))
    
@bot.command() 
async def cajas_de_carton(ctx):
    await ctx.send (random.choice(["https://www.youtube.com/watch?v=fBNcP5Z7PRQ",
    "https://www.youtube.com/watch?v=Cx2vm31y0IA",
    "https://www.youtube.com/watch?v=B4h-7WQFjSE",
    "https://www.youtube.com/watch?v=K51U5Ey5w2g",
    "https://www.youtube.com/watch?v=KditWFpzwj4",
    "https://www.youtube.com/watch?v=Y6Be22k8jBQ",
    "https://www.youtube.com/watch?v=7mrybIFLFXI",
    "https://www.youtube.com/watch?v=PH775_GabZU",
    "https://www.youtube.com/watch?v=YQkwy_FzxqA",
    "https://www.youtube.com/watch?v=bPZ4CE4_Qhk"]))

bot.run("MTIzMjg0MDcyODc5OTg3MTA5Nw.G0WslE.jQ830_o3uRkA8PT7Wd6jJhvYvE9kBx5nvsKYCM")



