base_cogumelos_50 = [
    # --- GRUPO 1: AMANITAS (Lamelas livres, esporada branca, presença de volva/anel) ---
    {'nome': 'Amanita phalloides', 'toxicidade': 'Mortal', 'caracteristicas': ['volva na base', 'anel no estipe', 'lamelas livres', 'chapeu esverdeado']},
    {'nome': 'Amanita muscaria', 'toxicidade': 'Venenoso', 'caracteristicas': ['chapeu vermelho', 'verrugas brancas', 'estipe bulboso', 'bosque de coniferas']},
    {'nome': 'Amanita pantherina', 'toxicidade': 'Venenoso', 'caracteristicas': ['chapeu marrom', 'verrugas brancas', 'anel presente', 'colar na volva']},
    {'nome': 'Amanita caesarea', 'toxicidade': 'Comestivel', 'caracteristicas': ['chapeu laranja', 'lamelas amarelas', 'volva em saco', 'sem verrugas']},
    {'nome': 'Amanita virosa', 'toxicidade': 'Mortal', 'caracteristicas': ['inteiro branco', 'chapeu conico', 'anel fragil', 'volva profunda']},
    {'nome': 'Amanita rubescens', 'toxicidade': 'Comestivel (Cozido)', 'caracteristicas': ['carne que avermelha', 'verrugas cinzas', 'estipe robusto']},

    # --- GRUPO 2: AGARICUS E SIMILARES (Lamelas que escurecem, anel presente) ---
    {'nome': 'Agaricus bisporus', 'toxicidade': 'Comestivel', 'caracteristicas': ['chapeu branco', 'lamelas rosadas', 'cheiro fungico', 'comercial']},
    {'nome': 'Agaricus campestris', 'toxicidade': 'Comestivel', 'caracteristicas': ['campo aberto', 'lamelas marrom-escuras', 'anel simples', 'base estreita']},
    {'nome': 'Agaricus xanthodermus', 'toxicidade': 'Toxico', 'caracteristicas': ['amarela ao toque', 'cheiro de fenol', 'anel duplo', 'base bulbosa']},
    {'nome': 'Chlorophyllum molybdites', 'toxicidade': 'Venenoso', 'caracteristicas': ['esporada verde', 'escamas marrons', 'chapeu grande', 'gramados']},
    {'nome': 'Macrolepiota procera', 'toxicidade': 'Comestivel', 'caracteristicas': ['estipe longo', 'anel movel', 'chapeu escamoso', 'grande porte']},

    # --- GRUPO 3: BOLETOS (Himênio com poros/tubos em vez de lamelas) ---
    {'nome': 'Boletus edulis', 'toxicidade': 'Comestivel', 'caracteristicas': ['poros brancos', 'estipe reticulado', 'chapeu marrom', 'carne firme']},
    {'nome': 'Boletus satanas', 'toxicidade': 'Venenoso', 'caracteristicas': ['estipe vermelho', 'chapeu cinza-claro', 'azula ao corte', 'cheiro ruim']},
    {'nome': 'Suillus luteus', 'toxicidade': 'Comestivel', 'caracteristicas': ['chapeu viscoso', 'anel presente', 'poros amarelos', 'simbiose com pinus']},
    {'nome': 'Tylopilus felleus', 'toxicidade': 'Inpalatavel (Amargo)', 'caracteristicas': ['poros rosados', 'reticulado escuro', 'sabor muito amargo']},
    {'nome': 'Leccinum scabrum', 'toxicidade': 'Comestivel', 'caracteristicas': ['estipe com escamas pretas', 'chapeu marrom', 'sob bétulas']},

    # --- GRUPO 4: PSILOCYBES E COPRINUS (Psicotrópicos ou decompositores rápidos) ---
    {'nome': 'Psilocybe cubensis', 'toxicidade': 'Alucinogeno', 'caracteristicas': ['azula ao toque', 'cresce em esterco', 'chapeu dourado', 'anel persistente']},
    {'nome': 'Psilocybe semilanceata', 'toxicidade': 'Alucinogeno', 'caracteristicas': ['chapeu em bico', 'estipe flexivel', 'gramados umidos', 'pequeno']},
    {'nome': 'Coprinus comatus', 'toxicidade': 'Comestivel (Jovem)', 'caracteristicas': ['chapeu cilindrico', 'se transforma em tinta', 'escamas brancas']},
    {'nome': 'Coprinopsis atramentaria', 'toxicidade': 'Toxico com Alcool', 'caracteristicas': ['chapeu cinza', 'liso', 'antabuse', 'decompositor']},
    {'nome': 'Panaeolus cyanescens', 'toxicidade': 'Alucinogeno', 'caracteristicas': ['estipe fino', 'azula forte', 'lamelas manchadas', 'tropical']},

    # --- GRUPO 5: PLEUROTUS E LENTINULA (Crescem em madeira/troncos) ---
    {'nome': 'Pleurotus ostreatus', 'toxicidade': 'Comestivel', 'caracteristicas': ['formato de ostra', 'lamelas decorrentes', 'lateralizado', 'troncos']},
    {'nome': 'Lentinula edodes', 'toxicidade': 'Comestivel', 'caracteristicas': ['chapeu marrom escamoso', 'estipe rigido', 'cheiro forte', 'cultivo em toras']},
    {'nome': 'Pleurotus eryngii', 'toxicidade': 'Comestivel', 'caracteristicas': ['estipe grosso', 'chapeu pequeno marrom', 'lamelas descendo o caule']},
    {'nome': 'Omphalotus olearius', 'toxicidade': 'Venenoso', 'caracteristicas': ['cor laranja vivo', 'bioluminescente', 'lamelas decorrentes', 'base de oliveiras']},

    # --- GRUPO 6: CANTHARELLUS E HIDNUM (Formatos irregulares/espinhos) ---
    {'nome': 'Cantharellus cibarius', 'toxicidade': 'Comestivel', 'caracteristicas': ['cor amarela', 'cheiro de damasco', 'falsas lamelas', 'formato de funil']},
    {'nome': 'Hydnum repandum', 'toxicidade': 'Comestivel', 'caracteristicas': ['espinhos sob o chapeu', 'cor creme', 'carne quebradiça']},
    {'nome': 'Craterellus cornucopioides', 'toxicidade': 'Comestivel', 'caracteristicas': ['preto ou cinza', 'trombeta da morte', 'oco por dentro']},

    # --- GRUPO 7: POLIPOROS E MEDICINAIS (Duros ou texturas diferenciadas) ---
    {'nome': 'Ganoderma lucidum', 'toxicidade': 'Medicinal', 'caracteristicas': ['aspecto envernizado', 'rimiforme', 'cor de sangue seco', 'rigido']},
    {'nome': 'Hericium erinaceus', 'toxicidade': 'Medicinal/Comestivel', 'caracteristicas': ['franjas brancas pendentes', 'sem chapeu', 'aspecto de juba']},
    {'nome': 'Trametes versicolor', 'toxicidade': 'Medicinal', 'caracteristicas': ['forma de leque', 'zonas coloridas', 'textura coriacea', 'miudo']},
    {'nome': 'Fomes fomentarius', 'toxicidade': 'Inedivel', 'caracteristicas': ['forma de casco de cavalo', 'cinza', 'muito duro', 'em arvores mortas']},

    # --- GRUPO 8: OUTROS GÊNEROS IMPORTANTES ---
    {'nome': 'Galerina marginata', 'toxicidade': 'Mortal', 'caracteristicas': ['pequeno marrom', 'anel fragil', 'cresce em madeira', 'lamelas adnatas']},
    {'nome': 'Gyromitra esculenta', 'toxicidade': 'Mortal (Cru)', 'caracteristicas': ['chapeu cerebral', 'cor marrom-avermelhada', 'oco', 'primavera']},
    {'nome': 'Morchella esculenta', 'toxicidade': 'Comestivel (Cozido)', 'caracteristicas': ['aspecto de colmeia', 'chapeu alveolar', 'estipe oco']},
    {'nome': 'Russula emetica', 'toxicidade': 'Toxico', 'caracteristicas': ['chapeu vermelho vivo', 'lamelas brancas quebradiças', 'sabor ardido']},
    {'nome': 'Lactarius deliciosus', 'toxicidade': 'Comestivel', 'caracteristicas': ['emite latex laranja', 'zonas concentricas', 'sob pinheiros']},
    {'nome': 'Lactarius torminosus', 'toxicidade': 'Toxico', 'caracteristicas': ['latex branco', 'chapeu peludo na borda', 'rosa claro']},
    {'nome': 'Cortinarius orellanus', 'toxicidade': 'Mortal', 'caracteristicas': ['presença de cortina', 'cor de fogo/ferrugem', 'lamelas distantes']},
    {'nome': 'Hypholoma fasciculare', 'toxicidade': 'Venenoso', 'caracteristicas': ['amarelo enxofre', 'lamelas esverdeadas', 'sabor amargo', 'em tufos']},
    {'nome': 'Clitocybe dealbata', 'toxicidade': 'Mortal', 'caracteristicas': ['branco giz', 'chapeu plano ou funil', 'odor de farinha', 'gramados']},
    {'nome': 'Inocybe geophylla', 'toxicidade': 'Toxico', 'caracteristicas': ['chapeu conico', 'umbonado', 'cor lilas ou branca', 'lamelas acinzentadas']},
    {'nome': 'Ramaria flava', 'toxicidade': 'Comestivel (Cuidado)', 'caracteristicas': ['formato de coral', 'amarelo', 'pontas ramificadas']},
    {'nome': 'Lycoperdon perlatum', 'toxicidade': 'Comestivel (Jovem)', 'caracteristicas': ['formato de pera', 'solta esporos em pó', 'verrugas destacaveis']},
    {'nome': 'Calvatia gigantea', 'toxicidade': 'Comestivel', 'caracteristicas': ['bola gigante branca', 'liso', 'interior branco firme']},
    {'nome': 'Phallus impudicus', 'toxicidade': 'Inedivel', 'caracteristicas': ['formato falico', 'cheiro de carniça', 'atrai moscas', 'gleba verde']},
    {'nome': 'Sarcoscypha coccinea', 'toxicidade': 'Inofensivo', 'caracteristicas': ['formato de taça', 'vermelho escarlate', 'cresce em gravetos']},
    {'nome': 'Exidia glandulosa', 'toxicidade': 'Inofensivo', 'caracteristicas': ['textura gelatinosa', 'cor preta', 'forma irregular', 'umidade']},
    {'nome': 'Marasmius oreades', 'toxicidade': 'Comestivel', 'caracteristicas': ['aneis de fada', 'cheiro de amendoas', 'estipe flexivel', 'grama']},
    {'nome': 'Tremella mesenterica', 'toxicidade': 'Edivel', 'caracteristicas': ['gelatina amarela', 'forma de cerebro', 'parasita outros fungos']}
]

print('-- SISTEMA INTELIGENTE DE IDENTIFICAÇÃO DE COGUMELOS --')
print('O QUE DESEJA SABER? DIGITE O NÚMERO CORRESPONDENTE:\n' \
'1.Encontrar um cogumelo pelas características\n'
'2.Pesquisar por um cogumelo específico\n'
'3.Estimar a probabilidade de toxicidade\n'
'4.Pesquisar por grupos taxonômicos')
opcao = int(input('Digite a opção desejada: '))

def cog_corresp(base_cogumelos_50, carac_user):
    resultados = []
    for cogumelo in base_cogumelos_50:
        carac = cogumelo['caracteristicas']
        coincidencias = sum(1 for c in carac_user if c in carac)
        compatibilidade = coincidencias / len(carac_user) * 100

        resultados.append({
            'nome': cogumelo['nome'],
            'toxicidade': cogumelo['toxicidade'],
            'compatibilidade': compatibilidade,
            'coincidentes': [c for c in carac_user if c in carac],
            'faltantes': [c for c in carac_user if c not in carac]
        })
    
    resultados.sort(key=lambda x: x['compatibilidade'], reverse=True)
    return resultados[:3]

def cog_espec(base_cogumelos_50, entrada):
    encontrados = []
    for c in base_cogumelos_50: 
        if entrada.lower() in c['nome'].lower():
            encontrados.append(c)
    
    if encontrados:
        print('RESULTADOS: ')
        for c in encontrados:
            print(f'Nome: {c['nome']}')
            print(f'Toxicidade: {c['toxicidade']}')
            print('Características:', ','.join(c['caracteristicas']))
    
    else:
        print("Nenhum cogumelo encontrado com esse nome ou parte do nome.")

def prob_perigo_saude(base_cogumelos_50, carac_user):
    resultados = []
    for cogumelo in base_cogumelos_50:
        carac = cogumelo['caracteristicas']
        coincidencias = sum(1 for c in carac_user if c in carac)
        compatibilidade = coincidencias / len(carac_user) * 100

        resultados.append({
            'nome': cogumelo['nome'],
            'toxicidade': cogumelo['toxicidade'],
            'compatibilidade': compatibilidade
        })
    
    # ordenar pelos mais compatíveis
    resultados.sort(key=lambda x: x['compatibilidade'], reverse=True)
    top3 = resultados[:3]

    # definir quais toxicidades são consideradas perigosas
    perigosas = ['mortal', 'venenoso', 'toxico', 'toxico com alcool', 'inedivel']
    perigosos = [r for r in top3 if any(p in r['toxicidade'].lower() for p in perigosas)]

    prob = len(perigosos) / len(top3) * 100

    return top3, prob

if opcao == 1:
    entrada = input("Digite as características separadas por vírgula: ")
    carac_user = [c.strip() for c in entrada.split(",")]  # transforma em lista
    resultados = cog_corresp(base_cogumelos_50, carac_user)

    print("\n-- RESULTADOS --")
    for r in resultados:
        print(f"{r['nome']} - {r['toxicidade']} - Possui {r['compatibilidade']:.1f}% das caracteristicas fornecidas")
        print("Coincidentes:", r['coincidentes'])
        print("Faltantes:", r['faltantes'])
        print()

if opcao == 2:
    entrada = input("Digite o nome do cogumelo: ")
    cog_espec(base_cogumelos_50, entrada)

if opcao == 3:
    entrada = input("Digite as características separadas por vírgula: ")
    carac_user = [c.strip() for c in entrada.split(",")]
    top3, prob = prob_perigo_saude(base_cogumelos_50, carac_user)

    print("\n-- RESULTADOS --")
    for r in top3:
        print(f"{r['nome']} - {r['toxicidade']} ({r['compatibilidade']:.1f}% compatibilidade)")
    print(f"\nProbabilidade estimada de ser perigoso à saúde: {prob:.1f}%")


        