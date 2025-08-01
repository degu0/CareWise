#Sistema de pontoação para determinar se paciente tem a doença

#Diabetes
def calcular_pontuacao_diabetes(**kwargs):
    pontuacao = 0
    
    # Idade
    idade = kwargs.get('idade', 0)
    if idade >= 60:
        pontuacao += 10
    elif idade >= 45:
        pontuacao += 5
    
    # Glicemia em jejum
    glicemia_em_jejum = kwargs.get('glicemia_em_jejum', 0)
    if glicemia_em_jejum >= 200:
        pontuacao += 40
    elif glicemia_em_jejum >= 126:
        pontuacao += 30
    elif 100 <= glicemia_em_jejum < 126:
        pontuacao += 10
    
    # HbA1c
    hbA1c = kwargs.get('hbA1c', 0)
    if hbA1c >= 8.0:
        pontuacao += 40
    elif hbA1c >= 6.5:
        pontuacao += 30
    elif 5.7 <= hbA1c < 6.5:
        pontuacao += 10
    
    # TTGO
    ttgo = kwargs.get('ttgo', 0)
    if ttgo >= 200:
        pontuacao += 30
    elif 140 <= ttgo < 200:
        pontuacao += 10
    
    # IMC
    imc = kwargs.get('imc', 0)
    if imc >= 40:
        pontuacao += 30
    elif 35 <= imc < 40:
        pontuacao += 20
    elif 30 <= imc < 35:
        pontuacao += 10
    elif 25 <= imc < 30:
        pontuacao += 5
    
    # Atividade física
    atividade_fisica = kwargs.get('atividade_fisica', 0)
    if atividade_fisica == 1.0:  # Assumindo que 1.0 significa inativo
        pontuacao += 5
    
    # Álcool
    alcool = kwargs.get('alcool', 0)
    if alcool == 1.0:  # Assumindo que 1.0 significa consumo excessivo
        pontuacao += 5
    
    # Histórico familiar de diabetes
    historico_familiar_diabetes = kwargs.get('historico_familiar_diabetes', 0)
    if historico_familiar_diabetes == 1.0:  # Assumindo que 1.0 significa presente
        pontuacao += 10
    
    # Uso de medicamentos para diabetes
    uso_de_medicamentos_diabetes = kwargs.get('uso_de_medicamentos_diabetes', 0)
    if uso_de_medicamentos_diabetes == 1.0:  # Assumindo que 1.0 significa sim
        pontuacao += 50
    
    # Sintomas clássicos de diabetes
    sintomas_classicos_diabetes = kwargs.get('sintomas_classicos_diabetes', 0)
    if sintomas_classicos_diabetes == 1.0:  # Assumindo que 1.0 significa presente
        pontuacao += 15
    
    return pontuacao

#Hipertensao
def calcular_pontuacao_hipertensao(**kwargs):
    pontuacao = 0
    
    # Idade
    idade = kwargs.get('idade', 0)
    if idade >= 65:
        pontuacao += 10
    elif 45 <= idade < 65:
        pontuacao += 5
    
    # Pressão arterial sistólica (PAS)
    pas = kwargs.get('pas', 0)
    if pas >= 160:
        pontuacao += 25
    elif 140 <= pas < 160:
        pontuacao += 15
    elif 130 <= pas < 140:
        pontuacao += 5
    
    # Pressão arterial diastólica (PAD)
    pad = kwargs.get('pad', 0)
    if pad >= 100:
        pontuacao += 25
    elif 90 <= pad < 100:
        pontuacao += 15
    elif 80 <= pad < 90:
        pontuacao += 5
    
    # IMC
    imc = kwargs.get('imc', 0)
    if imc >= 35:
        pontuacao += 15
    elif 30 <= imc < 35:
        pontuacao += 10
    elif 25 <= imc < 30:
        pontuacao += 5
    
    # Atividade física
    if kwargs.get('atividade_fisica', 0) == 1.0:
        pontuacao += 5
    
    # Álcool
    if kwargs.get('alcool', 0) == 1.0:
        pontuacao += 5
    
    # Fumante
    if kwargs.get('fumante', 0) == 1.0:
        pontuacao += 15
    
    # Histórico familiar de hipertensão
    if kwargs.get('historico_familiar_hipertensao', 0) == 1.0:
        pontuacao += 10
    
    # Uso de medicamentos para hipertensão
    if kwargs.get('uso_de_medicamentos_hipertensao', 0) == 1.0:
        pontuacao += 40
    
    return pontuacao

#DRC
def calcular_pontuacao_drc(**kwargs):
    pontuacao = 0
    
    # Idade
    idade = kwargs.get('idade', 0)
    if idade >= 60:
        pontuacao += 5
    
    # Hipertensão
    if kwargs.get('hipertensao', 0) == 1.0:
        pontuacao += 20
    
    # Pressão sistólica
    pas = kwargs.get('pressao_sistolica', 0)
    if pas >= 160:
        pontuacao += 10
    elif 140 <= pas < 160:
        pontuacao += 5
    
    # Pressão diastólica
    pad = kwargs.get('pressao_diastolica', 0)
    if pad >= 100:
        pontuacao += 10
    elif 90 <= pad < 100:
        pontuacao += 5
    
    # Diabetes
    if kwargs.get('diabetes', 0) == 1.0:
        pontuacao += 20
    
    # Glicose (controle glicêmico ruim)
    glicose = kwargs.get('glicose', 0)
    if glicose >= 126 and kwargs.get('diabetes', 0) == 1.0:
        pontuacao += 5
    
    # Histórico familiar renal
    if kwargs.get('historico_familiar_renal', 0) == 1.0:
        pontuacao += 10
    
    # TFGe (Taxa de Filtração Glomerular Estimada)
    tfge = kwargs.get('tfge', 0)
    if tfge < 15:
        pontuacao += 70
    elif 15 <= tfge < 30:
        pontuacao += 50
    elif 30 <= tfge < 45:
        pontuacao += 30
    elif 45 <= tfge < 60:
        pontuacao += 20
    elif 60 <= tfge < 90:
        pontuacao += 10
    
    # Albuminúria
    albuminuria = kwargs.get('albuminuria', 0)
    if albuminuria == 1.0:  # Considerando binário (1.0 = grave)
        pontuacao += 40
    elif albuminuria >= 300:
        pontuacao += 40
    elif 30 <= albuminuria < 300:
        pontuacao += 20
    
    # Creatinina
    creatinina = kwargs.get('creatinina', 0)
    if creatinina >= 2.0:
        pontuacao += 30
    elif 1.5 <= creatinina < 2.0:
        pontuacao += 10
    
    # Ureia
    ureia = kwargs.get('ureia', 0)
    if ureia > kwargs.get('limite_ureia', 40):  # Assumindo 40 como limite superior
        pontuacao += 5
    
    # Hemoglobina
    hemoglobina = kwargs.get('hemoglobina', 0)
    if hemoglobina < 12:
        pontuacao += 10
    
    # Potássio
    potassio = kwargs.get('potassio', 0)
    if potassio >= 6.0:
        pontuacao += 20
    elif potassio >= 5.5:
        pontuacao += 10
    
    # Proteinúria
    if kwargs.get('proteinuria', 0) == 1.0:
        pontuacao += 30
    
    return pontuacao

#DCOP
def calcular_pontuacao_pulmonar(**kwargs):
    pontuacao = 0
    
    # Idade
    idade = kwargs.get('idade', 0)
    if idade >= 60:
        pontuacao += 10
    elif 40 <= idade < 60:
        pontuacao += 5
    
    # Fumante
    if kwargs.get('fumante', 0) == 1.0:
        pontuacao += 30
    
    # Ex-fumante
    if kwargs.get('ex_fumante', 0) == 1.0:
        pontuacao += 25
    
    # Exposição a poluentes
    if kwargs.get('exposicao_a_poluentes', 0) == 1.0:
        pontuacao += 15
    
    # Tosse
    if kwargs.get('tosse', 0) == 1.0:
        pontuacao += 10
    
    # Falta de ar
    if kwargs.get('falta_de_ar', 0) == 1.0:
        pontuacao += 15
    
    # Sibilância
    if kwargs.get('sibilancia', 0) == 1.0:
        pontuacao += 10
    
    # Capacidade pulmonar
    capacidade_pulmonar = kwargs.get('capacidade_pulmonar', 0)
    if capacidade_pulmonar < 0.70:  # Assumindo VEF1/CVF
        pontuacao += 20
    elif capacidade_pulmonar < 0.80:  # Assumindo capacidade pulmonar reduzida
        pontuacao += 10
    
    return pontuacao

#Asma
def calcular_pontuacao_asma(**kwargs):
    pontuacao = 0
    
    # Idade (infância/adolescência ou início tardio)
    idade = kwargs.get('idade', 0)
    if (idade < 18) or (idade > 40):  # Assumindo que início tardio é >40 anos
        pontuacao += 5
    
    # Exposição a alérgenos
    if kwargs.get('exposicao_alergenos', 0) == 1.0:
        pontuacao += 10
    
    # Fumante passivo
    if kwargs.get('fumante_passivo', 0) == 1.0:
        pontuacao += 10
    
    # Infecções respiratórias frequentes
    if kwargs.get('infeccoes_respiratorias_frequentes', 0) == 1.0:
        pontuacao += 10
    
    # Histórico familiar de asma
    if kwargs.get('historico_familiar_asma', 0) == 1.0:
        pontuacao += 15
    
    # Dispneia
    if kwargs.get('dispneia', 0) == 1.0:
        pontuacao += 15
    
    # Sibilância
    if kwargs.get('sibilancia', 0) == 1.0:
        pontuacao += 25
    
    # Tosse
    if kwargs.get('tosse', 0) == 1.0:
        pontuacao += 15
    
    # Obstrução de vias respiratórias
    if kwargs.get('obstrucao_vias_respiratorias', 0) == 1.0:
        pontuacao += 20
    
    return pontuacao

#Aids
def calcular_pontuacao_hiv(**kwargs):
    pontuacao = 0
    
    # Parceiros sexuais
    if kwargs.get('parceiros_sexuais', 0) > 1 or kwargs.get('parceiros_sexuais', 0) == 1.0:
        pontuacao += 5
    
    # Uso de preservativo
    if kwargs.get('uso_preservativo', 0) == 1.0:
        pontuacao -= 10  # Reduz o risco
    else:
        pontuacao += 10
    
    # Relação sexual sem proteção
    if kwargs.get('relacao_sexual_sem_protecao', 0) == 1.0:
        pontuacao += 20
    
    # Drogas injetáveis
    if kwargs.get('drogas_injetaveis', 0) == 1.0:
        pontuacao += 30
    
    # Transfusão sanguínea
    if kwargs.get('transfusao_sanguinea', 0) == 1.0:
        pontuacao += 20
    
    # Relação com pessoa HIV+
    if kwargs.get('relacao_com_pessoa_hiv', 0) == 1.0:
        pontuacao += 25
    
    # Sintomas iniciais
    if kwargs.get('sintomas_iniciais', 0) == 1.0:
        pontuacao += 10
    
    # Contagem de células CD4
    cd4 = kwargs.get('quantidade_celulas_por_milimetro_cubico', 0)
    if cd4 < 200:
        pontuacao += 50
    elif 200 <= cd4 < 500:
        pontuacao += 30
    
    return max(pontuacao, 0)  # Garante que não fique negativo

#Obesidade
def calcular_pontuacao_obesidade(**kwargs):
    pontuacao = 0
    
    # IMC (fator principal)
    imc = kwargs.get('imc', 0)
    if imc >= 40:
        pontuacao += 80
    elif 35 <= imc < 40:
        pontuacao += 60
    elif 30 <= imc < 35:
        pontuacao += 40
    elif 25 <= imc < 30:
        pontuacao += 20
    
    # Atividade física
    if kwargs.get('atividade_fisica', 0) == 1.0:  # 1.0 = inativo
        pontuacao += 10
    
    # Alimentação ruim
    if kwargs.get('alimentacao_ruim', 0) == 1.0:
        pontuacao += 15
    
    # Histórico familiar
    if kwargs.get('historico_familiar_obesidade', 0) == 1.0:
        pontuacao += 15
    
    # Distúrbio metabólico
    if kwargs.get('disturbio_metabolico', 0) == 1.0:
        pontuacao += 20
    
    return pontuacao

#Osteoporose
def calcular_pontuacao_osteoporose(**kwargs):
    pontuacao = 0
    
    # Idade
    idade = kwargs.get('idade', 0)
    if idade >= 65:
        pontuacao += 20
    elif 50 <= idade < 65:
        pontuacao += 10
    
    # Sexo (feminino)
    if kwargs.get('sexo', 1.0) == 0.0:  # Assumindo 0.0 = feminino
        pontuacao += 20
    
    # Atividade física
    if kwargs.get('atividade_fisica', 0) == 1.0:
        pontuacao += 5
    
    # Baixo peso
    if kwargs.get('baixo_peso', 0) == 1.0:
        pontuacao += 10
    
    # Deficiência de cálcio
    if kwargs.get('deficiencia_calcio', 0) == 1.0:
        pontuacao += 10
    
    # Deficiência de vitamina D
    if kwargs.get('deficiencia_vitamina_d', 0) == 1.0:
        pontuacao += 15
    
    # Histórico familiar ósseo
    if kwargs.get('historico_familiar_osseo', 0) == 1.0:
        pontuacao += 15
    
    # Fumante
    if kwargs.get('fumante', 0) == 1.0:
        pontuacao += 10
    
    # Álcool
    if kwargs.get('alcool', 0) == 1.0:
        pontuacao += 10
    
    # Doenças autoimunes
    if kwargs.get('doencas_autoimunes', 0) == 1.0:
        pontuacao += 10
    
    # Uso de corticoides
    if kwargs.get('uso_corticoides', 0) == 1.0:
        pontuacao += 20
    
    return pontuacao

#Cardiovascular
def calcular_pontuacao_cardiovascular(**kwargs):
    pontuacao = 0
    
    # Idade
    idade = kwargs.get('idade', 0)
    if idade >= 75:
        pontuacao += 30
    elif 60 <= idade < 75:
        pontuacao += 20
    elif 40 <= idade < 60:
        pontuacao += 10
    
    # Sexo (masculino)
    if kwargs.get('sexo', 0) == 1.0:  # Assumindo 1.0 = masculino
        pontuacao += 5
    
    # Fumante
    if kwargs.get('fumante', 0) == 1.0:
        pontuacao += 25
    
    # Obeso
    if kwargs.get('obeso', 0) == 1.0:
        pontuacao += 15
    
    # Colesterol alto
    if kwargs.get('colesterol_alto', 0) == 1.0:
        pontuacao += 15
    
    # Hipertensão
    if kwargs.get('hipertensao', 0) == 1.0:
        pontuacao += 20
    
    # Diabetes
    if kwargs.get('diabetes', 0) == 1.0:
        pontuacao += 20
    
    # Atividade física
    if kwargs.get('atividade_fisica', 0) == 1.0:
        pontuacao += 10
    
    # Histórico familiar cardiovascular
    if kwargs.get('historico_familiar_cardiovascular', 0) == 1.0:
        pontuacao += 15
    
    # Pressão sistólica
    pas = kwargs.get('pressao_sistolica', 0)
    if pas >= 160:
        pontuacao += 15
    elif 140 <= pas < 160:
        pontuacao += 5
    
    return pontuacao


# Função para imprimir resultados formatados
def imprimir_resultados(paciente):
    print("\n" + "="*50)
    print(f"RESULTADOS PARA PACIENTE: {paciente.get('nome', 'Não informado')}")
    print("="*50)
    
    doencas = {
        'Diabetes': calcular_pontuacao_diabetes,
        'Hipertensão': calcular_pontuacao_hipertensao,
        'Doença Renal Crônica': calcular_pontuacao_drc,
        'Doença Pulmonar (DCOP)': calcular_pontuacao_pulmonar,
        'Asma': calcular_pontuacao_asma,
        'HIV/AIDS': calcular_pontuacao_hiv,
        'Obesidade': calcular_pontuacao_obesidade,
        'Osteoporose': calcular_pontuacao_osteoporose,
        'Doença Cardiovascular': calcular_pontuacao_cardiovascular
    }
    
    for doenca, funcao in doencas.items():
        pontuacao = funcao(**paciente)
        print(f"\n{doenca.upper()}: {pontuacao} pontos")
        
        # Interpretação básica
        if doenca == 'Diabetes':
            if pontuacao >= 70: print("  → Risco muito alto (provável diabetes)")
            elif pontuacao >= 40: print("  → Risco alto (pré-diabetes ou diabetes não controlado)")
            elif pontuacao >= 20: print("  → Risco moderado")
            else: print("  → Risco baixo")
        
        elif doenca in ['Hipertensão', 'Doença Cardiovascular']:
            if pontuacao > 60: print("  → Risco muito alto")
            elif pontuacao > 30: print("  → Risco alto")
            else: print("  → Risco baixo/moderado")
        
        elif doenca == 'Obesidade':
            if pontuacao >= 60: print("  → Obesidade grave (Grau II/III)")
            elif pontuacao >= 40: print("  → Obesidade (Grau I)")
            elif pontuacao >= 20: print("  → Sobrepeso")
            else: print("  → Peso normal")
        
        else:  # Interpretação genérica para outras doenças
            if pontuacao > 50: print("  → Risco muito alto")
            elif pontuacao > 25: print("  → Risco alto")
            elif pontuacao > 10: print("  → Risco moderado")
            else: print("  → Risco baixo")

# Exemplo de uso
paciente_exemplo = {
    'nome': 'João da Silva',
    'idade': 58,
    'sexo': 1.0,  # masculino
    'imc': 32,
    'glicemia_em_jejum': 110,
    'hbA1c': 6.2,
    'pas': 148,
    'pad': 92,
    'atividade_fisica': 1.0,  # inativo
    'fumante': 1.0,
    'historico_familiar_diabetes': 1.0,
    'capacidade_pulmonar': 0.68,
    'albuminuria': 25,
    'tfge': 78,
    'uso_corticoides': 0.0,
    'colesterol_alto': 1.0
}

imprimir_resultados(paciente_exemplo)


