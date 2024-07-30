from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Base de dados de textos
abertura = [
    "Querida Larissa,",
    "Minha amada Larissa,",
    "Minha princesa,",
    "Minha vida,",
    "Minha musa,",
    "Minha luz,",
    "Com todo carinho,",
    "Com todo meu amor,",
    "Meu amor,",
    "Minha eterna paixão,",
    "Minha querida,",
    "Minha razão de viver,"
]

introducao = [
    "Não há palavras suficientes no mundo para expressar o quanto eu te amo e o quanto você significa para mim.",
    "Desde o momento em que nos conhecemos, minha vida mudou para melhor.",
    "Desde o instante em que nossos caminhos se cruzaram, eu percebi que havia encontrado algo verdadeiramente raro e precioso.",
    "Cada dia ao seu lado é uma nova aventura, e eu sou grato por ter você ao meu lado.",
    "Sua presença é como um campo de margaridas na primavera, simples e delicado, mas carregado de uma beleza que ilumina o mundo ao seu redor.",
    "Você é a razão do meu sorriso e da minha felicidade.",
    "Você é um presente tão especial que me parece um sonho.",
    "Às vezes me pego apenas te admirando, perdido em pensamentos sobre como Deus foi bondoso comigo em unir nossos caminhos e propósitos.",
    "Nada neste vasto cosmos pode chegar aos pés da sua beleza. Sua essência é única e inigualável.",
    "Desde que te conheci, minha vida tem sido um mar de felicidade e amor.",
    "Cada momento ao seu lado é um presente que agradeço todos os dias.",
    "Você trouxe luz e alegria para a minha vida de uma maneira que eu nunca imaginei possível.",
    "Você é a pessoa mais especial que já conheci, e sou eternamente grato por ter você ao meu lado.",
    "Te encontrar foi como encontrar um tesouro que eu nem sabia que estava procurando.",
    "Cada dia ao seu lado é um novo capítulo em nossa linda história de amor."
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
    "Você é minha inspiração diária, e cada momento ao seu lado é uma bênção.",
    "Seu sorriso ilumina meus dias, e sua voz é a melodia que acalma meu coração.",
    "Você é a pessoa que eu sempre sonhei em encontrar, e eu te amo mais a cada dia.",
    "Cada dia ao seu lado é um presente que eu agradeço todos os dias.",
    "Você faz a minha vida ser mais bonita e cheia de amor.",
    "Seu amor é a força que me guia e me dá coragem para enfrentar qualquer desafio.",
    "Você é a razão pela qual eu acordo todos os dias com um sorriso no rosto.",
    "Seu carinho e ternura fazem com que cada dia ao seu lado seja um sonho."
]

conclusao = [
    "Estou ansioso para todos os momentos que ainda temos pela frente.",
    "Vamos continuar construindo memórias maravilhosas juntos.",
    "Você é meu tudo, e mal posso esperar para passar o resto da minha vida ao seu lado.",
    "Você é a razão pela qual eu acordo todos os dias com um sorriso, e a certeza de que, ao seu lado, tudo é possível.",
    "Eu mal posso esperar para ver o que o futuro nos reserva.",
    "Juntos, podemos superar qualquer obstáculo e alcançar qualquer sonho.",
    "Eu te amo mais do que palavras podem expressar.",
    "Obrigado por ser a luz da minha vida.",
    "Você é e sempre será o amor da minha vida.",
    "Nossa história de amor está apenas começando, e eu estou animado para ver o que vem a seguir.",
    "Você é meu companheiro de vida, e juntos, somos invencíveis.",
    "O amor que sinto por você cresce a cada dia, e mal posso esperar para ver onde essa jornada nos levará.",
    "Com você ao meu lado, sinto que posso enfrentar qualquer desafio que a vida nos apresente.",
    "Obrigado por ser a pessoa maravilhosa que você é e por compartilhar sua vida comigo.",
    "Cada momento ao seu lado é uma bênção, e eu sou grato por cada segundo.",
    "O futuro é brilhante porque eu tenho você ao meu lado."
]

encerramento = [
    "Com todo o meu amor, Kevyn",
    "Para sempre seu, Kevyn",
    "Com carinho, Kevyn",
    "Com amor eterno, Kevyn",
    "Sempre seu, Kevyn",
    "Com todo meu carinho, Kevyn",
    "Amorosamente, Kevyn",
    "Com amor infinito, Kevyn",
    "Seu para sempre, Kevyn",
    "Com todo meu coração, Kevyn",
    "Para sempre seu, com amor, Kevyn",
    "Com toda a minha devoção, Kevyn"
]

# Função para gerar o texto da carta
def gerar_texto_variado(num_paragrafos):
    texto_final = []

    # Adiciona a frase de abertura
    texto_final.append(random.choice(abertura))

    # Gera os parágrafos
    paragrafos = []
    for _ in range(num_paragrafos):
        if len(paragrafos) % 3 == 0:
            paragrafos.extend(random.sample(introducao, 1))
        elif len(paragrafos) % 3 == 1:
            paragrafos.extend(random.sample(desenvolvimento, 1))
        else:
            paragrafos.extend(random.sample(conclusao, 1))

    texto_final.extend(paragrafos)

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
