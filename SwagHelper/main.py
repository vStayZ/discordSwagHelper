import discord
import STATIC
import asyncio
import random

bot = discord.Client()


def is_not_pinned(mess):
    return not mess.pinned

@bot.event
async def on_ready():
    global giveaway
    global helpmessagebool

    print("\n" * 50)
    print(f"{bot.user} is now Online!")
    for i in bot.guilds:
        print(f"Connected on: {i.name}")
    bot.loop.create_task(task_game())

    ### Giveaway ###
    giveaway = False

async def task_game():
    while True:
        await bot.change_presence(activity=discord.Game("Listening to the Dictators"), status=discord.Status.online)
        await asyncio.sleep(12)
        await bot.change_presence(activity=discord.Game("Thanks vStayZ#6018 for making me :p"), status=discord.Status.online)
        await asyncio.sleep(12)
        await bot.change_presence(activity=discord.Game("Welcome to Swag Nation"), status=discord.Status.online)
        await asyncio.sleep(12)
        await bot.change_presence(activity=discord.Game("Enjoy your stay!"), status=discord.Status.online)
        await asyncio.sleep(12)

########################################################################################################################

@bot.event
async def on_member_join(member):
    if bot != member:
        channel = bot.get_channel(731446169640763434) #### Join member
        embed = discord.Embed(color=0xacd7f2,
                              description=f"<:rainbow1:740727367747764327> Welcome! {member.mention} <:rainbow1:740727367747764327>\n\n"
                                          "<:bluebullet:740177592572706838> i n f o <:bluebullet:740177592572706838>\n\n"
                                          "<a:arrow1:744505885300097114> Please read the rules in #ʚ🌱ɞ┇verify-n-rules\n\n"
                                          "<a:arrow1:744505885300097114> Get some roles in #ʚ🌼ɞ┇get-rolez\n\n"
                                          "<a:arrow1:744505885300097114> Any questions? Visit #╰・₊˚🥀・tickets\n\n"
                                          "<a:arrow1:744505885300097114> We have many fun bots and a nice community!\n\n"
                                          "<a:arrow1:744505885300097114> Please abide by the rules, it makes us a better community.\n\n"
                                          "<a:arrow1:744505885300097114> We have a shop! View it in #ʚ🛒ɞ┇shop\n\n"
                                          "<a:arrow1:744505885300097114> Do you have something to help us improve? Place it in #╰・₊˚💫・feedback!\n\n"
                                          "<a:AiyuDeveloper:744506692766793748> That's basically it! Please contact Evan for more help on the server.\n\n"
                                          "<a:rainbow_heart:744506038853566495> Thank you for Joining! <a:rainbow_heart:744506038853566495>")
        file = discord.File("image/gif/memberjoinwelcome.gif", filename="memberjoinwelcome.gif")
        embed.set_image(url="attachment://memberjoinwelcome.gif")
        await channel.send(file=file, embed=embed)

        role = "Unverified"
        role = discord.utils.get(member.guild.roles, name=role)
        await member.add_roles(role)

@bot.event
async def on_member_remove(member):
    if bot != member:
        channel = bot.get_channel(731679987089932288) ## Leave member
        membercount = len(member.guild.members) - 2
        embed = discord.Embed(title=f"**{member}** Left the server...", color=0xb9f2ac,
                              description=f"Sadly **{member}** has left the server.\n"
                                          f"We now have **{membercount}** users left.\n"
                                          "Please don't leave us I like all of you!")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        file = discord.File("image/gif/memberremovebye.gif", filename="memberremovebye.gif")
        embed.set_image(url="attachment://memberremovebye.gif")
        await channel.send(file=file, embed=embed)

########################################################################################################################

@bot.event
async def on_message(message):
    global helpmessage, random
    global reactionrolesystem
    global ticketmessage

    if message.content.startswith(STATIC.PREFIX) and not bot.user == message.author:
        Dictator = "Dictator"
        Lieutenant = "👨‍💻 | Lieutenant"
        TrialModPolice = "👨‍🏭 | Trial Mod/Police"
        Colonel = "🔨 | Colonel"
        Dictator = discord.utils.get(message.author.guild.roles, name=Dictator)
        Lieutenant = discord.utils.get(message.author.guild.roles, name=Lieutenant)
        TrialModPolice = discord.utils.get(message.author.guild.roles, name=TrialModPolice)
        Colonel = discord.utils.get(message.author.guild.roles, name=Colonel)
        invoke = message.content[len(STATIC.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]

        invokelower = invoke.lower()

        #### Bot setup video ####
        if invokelower == "bot_setup" and Dictator in message.author.roles or invokelower == "bot_setup" and Lieutenant in message.author.roles  and not bot.user == message.author:
            await message.delete()
            send = await message.channel.send("Video: https://streamable.com/5pwvwq")
            await asyncio.sleep(300)
            await send.delete()

        if Dictator in message.author.roles or Lieutenant in message.author.roles or TrialModPolice in message.author.roles or Colonel in message.author.roles and not bot.user == message.author:

            #### HELP SYSTEM ####
            if invokelower == "help":
                await message.delete()
                embed = discord.Embed(title="<a:AiyuDeveloper:744506692766793748> **Admin Help Page 1/2**",
                                      color=discord.Color.blurple(),
                                      description="<a:arrow1:744505885300097114> s!help | Shows the help page\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!help\n\n"
                                                  "<a:arrow1:744505885300097114> s!say <message> | Makes the bot say something\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!say potato\n\n"
                                                  "<a:arrow1:744505885300097114> s!giveaway | Starts a giveaway\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!giveaway name\n\n"
                                                  "<a:arrow1:744505885300097114> s!giveaway done | Ends a giveaway\n"
                                                  "<a:rainbow_heart:744506038853566495>  Usage: s!giveaway done\n\n"
                                                  "<a:arrow1:744505885300097114> s!reaction_role | Start for reaction_role\n"
                                                  "<a:rainbow_heart:744506038853566495>  Usage: s!reaction_role\n\n"
                                                  "<a:arrow1:744505885300097114> s!bot_setup | Shows the bot-setup Video\n"
                                                  "<a:rainbow_heart:744506038853566495>  Usage: s!bot_setup\n\n"
                                                  "\nPage 2 -> ➡️\n"
                                                  f"{message.author.mention}")
                embed.set_footer(text="Prefix: s!")
                helpmessage = await message.channel.send(embed=embed)
                await helpmessage.add_reaction("❌")
                await helpmessage.add_reaction("➡️")
                await asyncio.sleep(180)
                await helpmessage.delete()

            #### Purge Chat System ####
            if invokelower == "purge":
                if int(args[0]) >= 1:
                    if args[0].isdigit():
                        count = int(args[0]) + 1

                        deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                        dell = len(deleted) - 1
                        embed = discord.Embed(title=f"Purged {dell} message(s)",
                                              description=f"**{message.author.name}** purged **{dell}** message(s) from the chat.")
                        file = discord.File("image/gif/purge.gif", filename="purge.gif")
                        embed.set_thumbnail(url="attachment://purge.gif")
                        send = await message.channel.send(embed=embed, file=file)
                        await asyncio.sleep(18)
                        await send.delete()
            #### say ####
            if invokelower == "say" and len(args[0]) >= 1:
                await message.delete()
                content = message.content.replace("s!say", "")
                await message.channel.send(f"{content}")

            #### Kick System ####
            if invokelower == "kick":
                try:
                    if len(args[0]) >= 1:
                        await message.delete()
                        member = discord.utils.find(lambda m: args[0] in m.name, message.guild.members)
                        if member:
                            if member == bot.user:
                                return
                            else:
                                await member.kick()
                                dm = await message.author.create_dm()
                                await dm.send(f"{member} kicked!")
                        else:
                            dm = await message.author.create_dm()
                            await dm.send(f"User not found!")
                except:
                    await message.delete()
                    send = await message.channel.send("You didn't provide enough parameters!")
                    await asyncio.sleep(12)
                    await send.delete()

            #### ban System ####
            if invokelower == "ban":
                try:
                    if len(args[0]) >= 1:
                        await message.delete()
                        member = discord.utils.find(lambda m: args[0] in m.name, message.guild.members)
                        if member:
                            if member == bot.user:
                                return
                            else:
                                await member.ban()
                                dm = await message.author.create_dm()
                                await dm.send(f"{member} banned!")
                        else:
                            dm = await message.author.create_dm()
                            await dm.send(f"User not found!")
                except:
                    await message.delete()
                    send = await message.channel.send("You didn't provide enough parameters!")
                    await asyncio.sleep(12)
                    await send.delete()

            #### muteSystem ####
            if invokelower == "mute":
                try:
                    if len(args[0]) >= 1:
                        await message.delete()
                        member = discord.utils.find(lambda m: args[0] in m.name, message.guild.members)
                        if member:
                            if member == bot.user:
                                return
                            else:
                                role = "Muted"
                                role = discord.utils.get(message.guild.roles, name=role)
                                await member.add_roles(role)

                                dm = await message.author.create_dm()
                                await dm.send(f"{member} muted!")
                        else:
                            dm = await message.author.create_dm()
                            await dm.send(f"User not found!")
                except:
                    await message.delete()
                    send = await message.channel.send("You didn't provide enough parameters!")
                    await asyncio.sleep(12)
                    await send.delete()

            if invokelower == "unmute":
                try:
                    if len(args[0]) >= 1:
                        await message.delete()
                        member = discord.utils.find(lambda m: args[0] in m.name, message.guild.members)
                        if member:
                            if member == bot.user:
                                return
                            else:
                                role = "Muted"
                                role = discord.utils.get(message.guild.roles, name=role)
                                await member.remove_roles(role)

                                dm = await message.author.create_dm()
                                await dm.send(f"{member} unmuted!")
                        else:
                            dm = await message.author.create_dm()
                            await dm.send(f"User not found!")
                except:
                    await message.delete()
                    send = await message.channel.send("You didn't provide enough parameters!")
                    await asyncio.sleep(12)
                    await send.delete()

        #### No Permission ####
        #else:
        #    await message.delete()
        #    send = await message.channel.send(f"Hey {message.author.mention} \nYou don't have the required permissions to execute this command!")
        #    await asyncio.sleep(10)
        #    await send.delete()

        #### Random meme ####
        if invokelower == "meme" or invokelower == "memes":
            if message.channel.id == 728817813011300422: #### meme channel
                memes = ["lehrerapple.jpg", "minecraftmeme4k.jpg", "boysandgirlswarzone.jpg", "fixedthebug.png", "simsonall.jpg", "eat3D.jpg",
                         "howtomakeyorcomputerrunfaster.png", "frog.jpg", "man.jpg", "manclass.jpg", "bare.jpg", "pokemonpikachu.jpg", "cryinghelp.jpg"]
                meme = random.choice(memes)
                file = discord.File(f"image/meme/{meme}", f"{meme}")
                await message.channel.send(file=file)

        #### Invite System ####
        if invokelower == "invite":
            await message.delete()
            error = await message.author.create_dm()
            await error.send("You wanted an invite link? Here have fun!\n"
                             "https://discord.gg/HM6cDh8")

        #### Server Stats System ####
        if invokelower == "server":
            guild = 728798787350298645  #### guild id
            guildcreate = bot.get_guild(guild)

            await message.delete()
            embed = discord.Embed(color=0xd3a9eb, timestamp=message.created_at)
            embed.set_author(name=f"{bot.get_guild(guild)}")
            embed.set_thumbnail(url=f"{guildcreate.icon_url}")
            embed.add_field(name=f"🗣️ Members", value=f"**{len(message.guild.members) - 2} Users**")
            embed.add_field(name="<a:AiyuDeveloper:744506692766793748> Server created",
                            value=f"**{guildcreate.created_at.strftime('%m.%d.%Y')}**")
            send = await message.channel.send(embed=embed)
            await asyncio.sleep(16)
            await send.delete()

    #### Verify System ####
    if message.content == "wA6^.-G" and not bot.user == message.author:
        if message.channel.id == 728944852426817556: ## Verify Channel
            role = "Unverified"
            role = discord.utils.get(message.author.guild.roles, name=role)

            if role in message.author.roles:
                await message.delete()
                await message.author.remove_roles(role)

                role = "🌎 | Comrade"
                print("2")
                role = discord.utils.get(message.author.guild.roles, name=role)
                print("3")
                await message.author.add_roles(role)
            else:
                await message.delete()
                error = await message.author.create_dm()
                await error.send("You're already verified...")
        else:
            await message.delete()

    #### Hello/Hi message ####
    hellocontent = message.content.lower()
    if hellocontent == "hello" or hellocontent == "hi" and not bot.user == message.author:
        array = [f"Hello {message.author.mention} :)", f"Hi {message.author.mention}", f"How are you? {message.author.mention}",
                 f"Oh hey {message.author.mention}", f"Hey {message.author.mention}, nice profile picture!", f"Hey {message.author.mention}! i hope you are fine :)"]
        await message.channel.send(f"{random.choice(array)}")

    #### BLACKLIST System ####
    import BLACKLIST
    for i in BLACKLIST.BLOCK:
        if i in message.content.strip().lower():
            await message.delete()

@bot.event
async def on_reaction_add(reaction, user):
        global helpmessage2

        #### Help System Reaction ADD ####
        if helpmessage.id:
            message = bot.get_channel(helpmessage.channel.id)
            if bot.user == user:
                return
            if reaction.emoji == "❌":
                try:
                    if helpmessage:
                        await helpmessage.delete()
                except:
                    if helpmessage2:
                        await helpmessage2.delete()
            elif reaction.emoji == "➡️":
                await helpmessage.delete()
                embed = discord.Embed(title="<a:AiyuDeveloper:744506692766793748> **Admin Help Page 2/2**",
                                      color=discord.Color.blurple(),
                                      description="<a:arrow1:744505885300097114> s!purge | Purges a certain number of messages\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!purge 4\n\n"
                                                  "<a:arrow1:744505885300097114> s!kick | Kicks a user\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!kick @loser\n\n"
                                                  "<a:arrow1:744505885300097114> s!ban | Bans a user\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!ban @begone\n\n"
                                                  "<a:arrow1:744505885300097114> s!mute | Mutes a member\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!mute @swag\n\n"
                                                  "<a:arrow1:744505885300097114> s!unmute | Unmutes a member\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!unmute @swag\n\n"
                                                  "<a:arrow1:744505885300097114> s!server | Stats from Bot and Server\n"
                                                  "<a:rainbow_heart:744506038853566495> Usage: s!server\n\n")
                embed.set_footer(text="Prefix: s!")
                helpmessage2 = await message.send(embed=embed)
                await helpmessage2.add_reaction("❌")
                await asyncio.sleep(180)
                await helpmessage2.delete()


bot.run(STATIC.TOKEN)