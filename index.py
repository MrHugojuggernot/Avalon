import discord
from manager import *
import os
TOKEN = 'NzkwODY1MTQ3NjgwOTE1NDU3.X-G0kA.taxWAbALyOU20SA5Ys4nnWBB95c'
client = discord.Client()

#config


@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


    if message.content.startswith("?search"):
        aya=message.content[7:]
        L=zasearch(aya[1:])
        embed= discord.Embed(title="Résultat pour **"+ str(aya) +"**",description="Nb de résultat : "+str(len(L)),color=0x00ff00)
        for index,element in enumerate(L):
            embed.add_field(name="Nom : "+str(L[index][1]), value="ID : "+ str(L[index][0]), inline=True)
        await channel.send(embed=embed)
        
    if message.content.startswith("?get"):
        ID=message.content.split()
        ID=ID[1]
        print("ok")
        os.chdir("Wallpaper_list")
        if str(ID)+".jpg" in os.listdir():
            os.chdir("..")
            name=show(int(ID)-1)
            print("trouvé!")
            os.chdir("Wallpaper_list")
            embed= discord.Embed(title="Affichage de **"+ str(name[1]) +"**",description="ID : "+str(name[0]),color=0x00ff00,image=str(ID)+".jpg")
            img= discord.File(str(ID)+".jpg",str(name[1]+".jpg"))
            await channel.send(embed=embed,file=img)
            os.chdir("..")
        else:
            await channel.send("Pas d'entrée correspondante pour l'identifiant: **"+str(ID)+"**")   
            os.chdir("..")



    if message.content.startswith("?add"):    
        aya=message.attachments
        title=message.content[5:]
        for i in search(title):
            if i == title:
                await channel.send(title+" est déjà un nom dans le db. Il faut en choisir un autre")
                break
        if len(aya) == 1:
            nb=ln()
            add(title)
            os.chdir("Wallpaper_list")
            await aya[0].save(str(nb)+".jpg")
            await channel.send("Ajout de : **"+message.content[5:]+"** avec l'ID : **"+str(nb)+"** dans la db !")
            os.chdir("..")

        else:
            await channel.send("Pas d'image envoyée ou > 1")






@client.event
async def on_ready():
    print('Avalon Wallpaper Manager :')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
