import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

trivia_questions = [
    {
        "pregunta": "¿Cuál es la mejor manera de ahorrar agua en casa?",
        "opciones": {
            "a": "Cerrar el grifo mientras te cepillas los dientes.",
            "b": "Lavar el coche todos los días.",
            "c": "Regar el jardín al mediodía.",
            "d": "Dejar el grifo abierto todo el día."
        },
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué es mejor para el medio ambiente, reutilizar o reciclar?",
        "opciones": {
            "a": "Reciclar siempre.",
            "b": "Reutilizar",
            "c": "No importa, son iguales.",
            "d": "Comprar productos nuevos."
        },
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál de las siguientes opciones es más sostenible: usar una botella de plástico o una botella reutilizable?",
        "opciones": {
            "a": "Botella de plástico.",
            "b": "Botella reutilizable.",
            "c": "Botella de vidrio desechable.",
            "d": "No usar botellas."
        },
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué tipo de energía es renovable?",
        "opciones": {
            "a": "Energía nuclear.",
            "b": "Energía solar.",
            "c": "Carbón.",
            "d": "Petróleo."
        },
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál es una manera eficaz de reducir la contaminación del aire?",
        "opciones": {
            "a": "Usar transporte público o bicicleta.",
            "b": "Conducir autos grandes todo el tiempo.",
            "c": "Quemar basura.",
            "d": "Usar aerosoles."
        },
        "respuesta": "a"
    }
]

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy Ecotrivia, un bot de Discord que te hará trivias sobre cómo proteger la naturaleza.')

@client.command()
async def trivia(ctx):
    question = random.choice(trivia_questions)
    opciones_texto = '\n'.join([f"{letra}: {opcion}" for letra, opcion in question["opciones"].items()])

    await ctx.send(f"{question['pregunta']}\n{opciones_texto}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['a', 'b', 'c', 'd']

    respuesta = await client.wait_for('message', check=check)
    
    if respuesta.content.lower() == question["respuesta"]:
        await ctx.send("¡Correcto! 🎉")
    else:
        respuesta_correcta = question["opciones"][question["respuesta"]]
        await ctx.send(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}")


client.run("TOKEN")
