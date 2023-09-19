import face_recognition


# Função para carregar e processar uma imagem
def carregar_imagem(caminho):
    imagem = face_recognition.load_image_file(caminho)
    return imagem


# Função para identificar os rostos presentes na imagem
def identificar_pessoas(imagem, descritores_conhecidos, nomes_conhecidos):
    # Detectar rostos na imagem
    faces = face_recognition.face_locations(imagem)

    if len(faces) == 0:
        return "Nenhum rosto foi detectado."

    # Extrair descritores de rosto da imagem atual
    descritor_imagem = face_recognition.face_encodings(imagem, faces)

    # Inicializar uma lista para os nomes identificados
    nomes_identificados = []

    for descritor in descritor_imagem:
        # Comparar com os descritores de rosto conhecidos
        coincidencias = face_recognition.compare_faces(descritores_conhecidos, descritor, tolerance=0.6)

        nome_identificado = "Desconhecido"  # Inicialmente, assuma como "Desconhecido"

        # Se uma correspondência foi encontrada, use o nome correspondente
        if True in coincidencias:
            index = coincidencias.index(True)
            nome_identificado = nomes_conhecidos[index]

        nomes_identificados.append(nome_identificado)

    return nomes_identificados


# Função para identificar as pessoas ausentes na imagem
def identificar_ausentes(nomes_conhecidos, nomes_presentes):
    nomes_ausentes = []

    for nome in nomes_conhecidos:
        if nome not in nomes_presentes:
            nomes_ausentes.append(nome)

    return nomes_ausentes


# Caminho para a imagem que você deseja analisar (substitua pelo caminho correto)
imagem_caminho = "3pessoas.jpeg"  # Substitua pelo caminho da imagem "ney3"

# Carregar as imagens conhecidas (neymar, messi, cr7) e seus descritores
#imagem_neymar = "neymar.jpg"
#imagem_messi = "messi.jpg"
#imagem_cr7 = "cr7.jpg"
#imagem_adriano = "adriano.jpeg"
#imagem_bianca = "bianca.jpeg"
imagem_brayan = "brayan.jpeg"
#imagem_davi = "davi.jpeg"
#imagem_davis = "davis.jpeg"
#imagem_felipe = "felipe.jpeg"
#imagem_francisco = "francisco.jpeg"
imagem_gustavo = "gustavo.png"
#imagem_jessica = "jessica.jpeg"
imagem_tijolo = "tijolo.jpeg"
#imagem_joyce = "joyce.jpeg"
#imagem_josemarcus = ""
imagem_kauan = "kauan.png"
#imagem_lucas = "lucas.jpeg"
imagem_mikael = "mikael.jpeg"
imagem_otavio = "otavio.png"
imagem_pedro = "pedro.png"
#imagem_sarah = "sarah.jpeg"
#imagem_sthe = ""
#imagem_thiago = "thiago.jpeg"
#imagem_vitin = ""
imagem_vitor = "vitor.png"
#imagem_vitoria = "vitoria.jpeg"

#imagem_neymar = carregar_imagem(imagem_neymar)
#imagem_messi = carregar_imagem(imagem_messi)
#imagem_cr7 = carregar_imagem(imagem_cr7)
#imagem_adriano = carregar_imagem(imagem_adriano)
#imagem_bianca = carregar_imagem(imagem_bianca)
imagem_brayan = carregar_imagem(imagem_brayan)
#imagem_davi = carregar_imagem(imagem_davi)
#imagem_davis = carregar_imagem(imagem_davis)
#imagem_felipe = carregar_imagem(imagem_felipe)
#imagem_francisco = carregar_imagem(imagem_francisco)
imagem_gustavo = carregar_imagem(imagem_gustavo)
#imagem_jessica = carregar_imagem(imagem_jessica)
imagem_tijolo = carregar_imagem(imagem_tijolo)
#imagem_joyce = carregar_imagem(imagem_joyce)
#imagem_josemarcus = ""
imagem_kauan = carregar_imagem(imagem_kauan)
#imagem_lucas = carregar_imagem(imagem_lucas)
imagem_mikael = carregar_imagem(imagem_mikael)
imagem_otavio = carregar_imagem(imagem_otavio)
imagem_pedro = carregar_imagem(imagem_pedro)
#imagem_sarah = carregar_imagem(imagem_sarah)
#imagem_sthe = ""
#imagem_thiago = carregar_imagem(imagem_thiago)
#imagem_vitin = ""
imagem_vitor = carregar_imagem(imagem_vitor)
#imagem_vitoria = carregar_imagem(imagem_vitoria)


descritores_conhecidos = [
    #face_recognition.face_encodings(imagem_neymar)[0],
    #face_recognition.face_encodings(imagem_messi)[0],
    #face_recognition.face_encodings(imagem_cr7)[0],
    #face_recognition.face_encodings(imagem_adriano)[0],
    #face_recognition.face_encodings(imagem_bianca)[0],
    face_recognition.face_encodings(imagem_brayan)[0],
    #face_recognition.face_encodings(imagem_davi)[0],
    #face_recognition.face_encodings(imagem_davis)[0],
    #face_recognition.face_encodings(imagem_felipe)[0],
    #face_recognition.face_encodings(imagem_francisco)[0],
    face_recognition.face_encodings(imagem_gustavo)[0],
    #face_recognition.face_encodings(imagem_jessica)[0],
    face_recognition.face_encodings(imagem_tijolo)[0],
    #face_recognition.face_encodings(imagem_joyce)[0],
    #face_recognition.face_encodings(imagem_josemarcus)[0],
    face_recognition.face_encodings(imagem_kauan)[0],
    #face_recognition.face_encodings(imagem_lucas)[0],
    face_recognition.face_encodings(imagem_mikael)[0],
    face_recognition.face_encodings(imagem_otavio)[0],
    #face_recognition.face_encodings(imagem_pedro)[0],
    #face_recognition.face_encodings(imagem_sarah)[0],
    #face_recognition.face_encodings(imagem_sthe)[0],
    #face_recognition.face_encodings(imagem_thiago)[0],
    #face_recognition.face_encodings(imagem_vitin)[0],
    face_recognition.face_encodings(imagem_vitor)[0],
    #face_recognition.face_encodings(imagem_vitoria)[0]

]

nomes_conhecidos = ["Brayan", "Gustavo", "Tijolo", "Kauan", "Mikael", "Otavio", "Pedro", "Vitor"]


# Carregar a imagem que você deseja analisar
imagem_analisar = carregar_imagem(imagem_caminho)

# Identificar as pessoas presentes na imagem e seus nomes
nomes_presentes = identificar_pessoas(imagem_analisar, descritores_conhecidos, nomes_conhecidos)

# Imprimir os nomes das pessoas presentes
print("Pessoas presentes na foto:")
for nome in nomes_presentes:
    print(nome)

# Identificar as pessoas ausentes e imprimir seus nomes
nomes_ausentes = identificar_ausentes(nomes_conhecidos, nomes_presentes)
print("\nPessoas ausentes na foto:")
for nome in nomes_ausentes:
    print(nome)
