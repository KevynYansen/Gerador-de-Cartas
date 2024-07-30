from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Base de dados de textos
abertura = [
    "Querida Larissa,",
    "Minha amada Larissa,",
    "Minha princesa",
    "Minha vida",
    "Minha musa",
    "Minha luz",
    "Com todo carinho",
    "Com todo meu amor",
    "Meu amor,"
]

introducao = [
    "Não há palavras suficientes no mundo para expressar o quanto eu te amo e o quanto você signfica para mim.",
    "Desde o momento em que nos conhecemos, minha vida mudou para melhor.",
    "Desde o instante em que nossos caminhos se cruzaram, eu percebi que havia encontrado algo verdadeiramente raro e precioso.",
    "Cada dia ao seu lado é uma nova aventura, e eu sou grato por ter você ao meu lado.",
    "Sua presença é como um campo de margaridas na primavera, simples e delicado, mas carregado de uma beleza que ilumina o mundo ao seu redor.",
    "Você é a razão do meu sorriso e da minha felicidade.",
    "Você é um presente tão especial que me parece um sonho.",
    "Às vezes me pego apenas te admirando, perdido em pensamentos sobre como Deus foi bondoso comigo em unir nosso caminhos e propósitos.",
    "Nada neste vasto cosmos pode chegar aos pés da sua beleza. Sua essência é única e inigualável."
]

desenvolvimento = [
    "Agradeço por cada momento que passamos juntos, desde os mais simples até os mais especiais.",
    "Os dias que passamos juntos são sempre cheios de alegria e amor, e eu valorizo cada um deles.",
    "Cada dia ao seu lado é uma nova descoberta, e o amor que sinto por você é como o céu noturno, infinito e profundo.",
    "Sob as estrelas que brilham em uma dança eterna, eu vejo a sua beleza refletida em cada astro, e percebo que nenhuma luz no universo pode se comparar à sua radiante presença.",
    "Quando olho para o céu coberto de estrelas, é como se cada ponto de luz fosse um lembrete de quão especial você é para mim.",
    "Seus olhos, que brilham com uma luz própria, têm o poder de ofuscar o brilho dos astros, tornando-os meros espectadores da verdadeira majestade que é você.",
    "Você é minha razão de viver, prometo que sempre estarei aqui.",
    "Sua presença traz luz e alegria para minha vida de uma maneira que ninguém consegue.",
    "Seu carinho e apoio são o que me motivam todos os dias, e eu sou eternamente grato por isso.",
    "Seus olhos, que brilham com uma luz própria, têm o poder de ofuscar o brilho dos astros, ornando-os meros espectadores da verdadeira majestade que é você."
]

conclusao = [
    "Estou ansioso para todos os momentos que ainda temos pela frente.",
    "Vamos continuar construindo memórias maravilhosas juntos.",
    "Você é meu tudo, e mal posso esperar para passar o resto da minha vida ao seu lado.",
    "Você é a razão pela qual eu acordo todos os dias com um sorriso, e a certeza de que, ao seu lado.",
    "Eu mal posso esperar para ver o que o futuro nos reserva.",
    "Juntos, podemos superar qualquer obstáculo e alcançar qualquer sonho.",
    "Eu te amo mais do que palavras podem expressar.",
    "Obrigado por ser a luz da minha vida.",
    "Você é e sempre será o amor da minha vida.",
    "Nossa história de amor está apenas começando, e eu estou animado para ver o que vem a seguir."
]

encerramento = [
    "Com todo o meu amor, Kevyn",
    "Para sempre seu, Kevyn",
    "Com carinho, Kevyn",
    "Com amor eterno, Kevyn",
    "Sempre seu, Kevyn",
    "Com todo meu carinho, Kevyn",
    "Amorosamente, Kevyn"
]

# Função para gerar um parágrafo variado
def gerar_paragrafo(tipo):
    if tipo == 'introducao':
        return random.choice(introducao)
    elif tipo == 'desenvolvimento':
        return random.choice(desenvolvimento)
    elif tipo == 'conclusao':
        return random.choice(conclusao)
    else:
        return ""

# Função para gerar o texto da carta
def gerar_texto_variado(num_paragrafos):
    texto_final = []
    
    # Adiciona a frase de abertura
    texto_final.append(random.choice(abertura))
    
    # Gera os parágrafos
    for i in range(num_paragrafos):
        if i % 3 == 0:
            tipo_paragrafo = 'introducao'
        elif i % 3 == 1:
            tipo_paragrafo = 'desenvolvimento'
        else:
            tipo_paragrafo = 'conclusao'
        
        texto_final.append(gerar_paragrafo(tipo_paragrafo))
    
    # Adiciona a frase de encerramento
    texto_final.append(random.choice(encerramento))
    
    return "\n\n".join(texto_final)

# Função para gerar uma carta personalizada
def gerar_carta(nome_destinataria, nome_remetente, num_paragrafos=15):
    carta = gerar_texto_variado(num_paragrafos)
    carta = carta.replace("[NOME]", nome_destinataria).replace("[SEU NOME]", nome_remetente)
    return carta

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        carta = gerar_carta("Larissa", "Kevyn")
        return render_template("result.html", carta=carta)
    return render_template("index.html")

@app.route("/gerar_carta", methods=["POST"])
def gerar_carta_ajax():
    carta = gerar_carta("Larissa", "Kevyn")
    return jsonify(carta=carta)

if __name__ == "__main__":
    app.run(debug=True)
