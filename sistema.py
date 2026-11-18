import re
import customtkinter as ctk


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

GREEN, MINT, INK, PAPER, MUTED = "#2D6A4F", "#52B788", "#1B4332", "#F4F6F4", "#6B7D72"

class Aplicativo(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Sistema de Cadastro de Voluntarios")
    self.geometry("900x600")

    # Permite que a linha e a coluna ocupem o espaço disponível
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    # Janela de abas
    self.janela_abas = ctk.CTkTabview(
      self, 
      width=600,
      segmented_button_fg_color=PAPER,
      segmented_button_font= ("Arial", 14, "normal"),
      segmented_button_selected_color=GREEN,
      segmented_button_selected_hover_color=GREEN,
      segmented_button_unselected_color=MUTED,
      segmented_button_unselected_hover_color=MUTED,
      text_color="white",
    )
    self.janela_abas.grid(row = 0,column = 0, sticky = "nsew")

    # Adicionar abas
    self.janela_abas.add("Login")
    self.janela_abas.add("Novo Cadastro")
    self.janela_abas.add("Perfil")


    # Criar as abas
    self.construir_login()  

    self.construir_novocadastro()

    self.construir_perfil()


  def construir_login(self):
    #Criando a aba de login
    aba_login = self.janela_abas.tab("Login")

    frame = ctk.CTkFrame(aba_login, fg_color=PAPER)
    frame.pack(fill="both", expand=True)
    lateral = ctk.CTkFrame(frame, fg_color=GREEN, corner_radius=0, width=480)
    lateral.pack(side="left", fill="y")
    lateral.pack_propagate(False)

    # Título lateral
    self.titulo_g = ctk.CTkLabel(
      lateral,
      text = "CONECTANDO\nVOLUNTÁRIOS",
      text_color="#D8F3DC",
      font = ("Arial", 30, "bold"),
      justify="left"
    )
    self.titulo_g.pack(anchor="w", padx=55, pady=(100, 20))


    self.titulo_m = ctk.CTkLabel(
      lateral,
      text = "Pequenas ações.\nGrandes transformações.",
      text_color="#D8F3DC",
      font = ("Arial", 20, "bold"),
      justify="left"
    )
    self.titulo_m.pack(anchor="w", padx=55)

    self.titulo_p = ctk.CTkLabel(
      lateral,
      text = "Um espaço para conectar pessoas\na causas que importam.",
      text_color="#D8F3DC",
      font = ("Arial", 15, "bold"),
      justify="left"
    )
    self.titulo_p.pack(anchor="w", padx=55, pady=(35, 0))

    self.texto_frameA = ctk.CTkLabel(
      frame, 
      text="Seja Bem-vindo!", 
      text_color=INK, 
      font=ctk.CTkFont(size=25, weight="bold")
    )
    self.texto_frameA.pack(padx=38, pady=(100, 5))

    self.texto_frameB = ctk.CTkLabel(
      frame, 
      text="Entre para continuar seu impacto.", 
      text_color=MUTED,
      font=ctk.CTkFont(size=13, weight="normal")
    )
    self.texto_frameB.pack(padx=38)

    # Campo de email
    self.label_email = ctk.CTkLabel(
      frame,
      text="E-mail:",
      font=("Arial", 16, "bold")
    )
    self.label_email.pack(pady=(5, 5))

    
    # Campo de entrada para o email
    self.campo_email = ctk.CTkEntry(
      frame,
      placeholder_text="Digite seu email",
      width=300,
      height=38
    )
    self.campo_email.pack(pady=(5, 10), padx=20)


    # Campo de senha
    self.label_senha = ctk.CTkLabel(
      frame,
      text="Senha:",
      font=("Arial", 16, "bold")
    )
    self.label_senha.pack(pady=(5, 5))

    # Campo de entrada para a senha
    self.campo_senha = ctk.CTkEntry(
      frame,
      placeholder_text="Digite sua senha",
      width=300,
      height=38,
      show="*"
    )
    self.campo_senha.pack(pady=(5, 10), padx=20)


    # Botão de entrar
    self.botao_entrar = ctk.CTkButton(
      frame,
      text="Entrar",
      fg_color = GREEN,
      hover_color = INK,
      width=300,
      height=38,
      command = self.entrar_perfil
    )

    self.botao_entrar.pack(pady=(5, 10), padx=20)


    # Campo de cadastro
    self.campo_cadastro = ctk.CTkButton(
      frame,
      text="Não tem uma conta? Cadastre-se",
      fg_color="transparent",
      text_color=INK,
      hover=False,
      command=lambda: self.janela_abas.set("Novo Cadastro")
    )

    self.campo_cadastro.pack(pady=(5, 10))



  def construir_novocadastro(self):

    #Criando a aba de novo cadastro
    aba_novocadastro = self.janela_abas.tab("Novo Cadastro")

    frame_cadastro = ctk.CTkFrame(aba_novocadastro, fg_color=MUTED, width=600)
    frame_cadastro.pack(fill="both", expand=True)

    # Título do cadastro
    self.titulo_cadastro = ctk.CTkLabel(
      frame_cadastro,
      text = "NOVO CADASTRO DE VOLUNTÁRIO",
      font = ("Arial", 20, "bold"),
      text_color=PAPER
    )
    self.titulo_cadastro.pack(anchor="nw", padx =10, pady=10)


    # Seção de Dados Pessoais
    self.dados_pessoais = ctk.CTkLabel(
      aba_novocadastro,
      text = "Dados Pessoais",
      font = ("Arial", 16, "bold")
    )
    self.dados_pessoais.pack(padx =10, pady=10)
    

    # Linha com Nome Completo e CPF lado a lado
    linha_nome_cpf = self.criar_linha(aba_novocadastro)
    linha_nome_cpf.pack_configure(padx=10)

    self.campo_nome = self.criar_campo(
      linha_nome_cpf,
      "Nome Completo",
      "Digite seu nome completo",
      400
    )

    self.campo_cpf_entrada = self.criar_campo(
      linha_nome_cpf,
      "CPF",
      "Digite seu CPF",
      200
    )

    # Linha com Data de Nascimento e Gênero
    linha_nascimento_genero = self.criar_linha(aba_novocadastro)
    linha_nascimento_genero.pack_configure(padx=10)

    self.campo_nascimento = self.criar_campo(
      linha_nascimento_genero,
      "Data de Nascimento",
      "DD/MM/AAAA",
      200
    )

    # Gênero é uma lista de opções (ComboBox), então é montado à mão
    coluna_genero = ctk.CTkFrame(linha_nascimento_genero, fg_color="transparent")
    coluna_genero.pack(side="left", fill="x", expand=True, padx=(0, 20))

    self.label_genero = ctk.CTkLabel(coluna_genero, text="Gênero", font=("Arial", 14))
    self.label_genero.pack(anchor="w", pady=(0, 5))

    self.campo_genero = ctk.CTkComboBox(
      coluna_genero,
      values=["Feminino", "Masculino", "Outro", "Prefiro não informar"],
      width=200
    )
    self.campo_genero.set("Selecione")
    self.campo_genero.pack(fill="x")


    # Seção de Contato
    self.contato = ctk.CTkLabel(
      aba_novocadastro,
      text="Contato",
      font=("Arial", 16, "bold")
    )
    self.contato.pack(anchor="nw", padx=10, pady=10)


    # Linha com E-mail e Telefone
    linha_email_telefone = self.criar_linha(aba_novocadastro)
    linha_email_telefone.pack_configure(padx=10)

    self.campo_email_cadastro = self.criar_campo(
      linha_email_telefone,
      "E-mail",
      "Digite seu e-mail",
      300
    )

    self.campo_telefone = self.criar_campo(
      linha_email_telefone,
      "Telefone",
      "(00) 00000-0000",
      200
    )


    # Linha com Endereço (sozinho)
    linha_endereco = self.criar_linha(aba_novocadastro)
    linha_endereco.pack_configure(padx=10)

    self.campo_endereco = self.criar_campo(
      linha_endereco,
      "Endereço Completo",
      "Rua, número, bairro, cidade",
      520
    )


    # Seção de Perfil
    self.perfil = ctk.CTkLabel(
      aba_novocadastro,
      text="Perfil",
      font=("Arial", 16, "bold")
    )
    self.perfil.pack(anchor="nw", padx=10, pady=10)


    # Interesses/Causas
    linha_interesses = self.criar_linha(aba_novocadastro)
    linha_interesses.pack_configure(padx=10)
    self.campo_interesses = self.criar_campo(
      linha_interesses,
      "Interesses/Causas",
      "Ex: Educação, Meio Ambiente",
      520
    )

    # Habilidades
    linha_habilidades = self.criar_linha(aba_novocadastro)
    linha_habilidades.pack_configure(padx=10)
    self.campo_habilidades = self.criar_campo(
      linha_habilidades,
      "Habilidades",
      "Ex: Comunicação, Informática",
      520
    )

    # Disponibilidade
    linha_disponibilidade = self.criar_linha(aba_novocadastro)
    linha_disponibilidade.pack_configure(padx=10)
    self.campo_disponibilidade = self.criar_campo(
      linha_disponibilidade,
      "Disponibilidade [dias/horários]",
      "Ex: Sábados, manhã",
      520
    )


    # Botões Salvar e Cancelar lado a lado
    linha_botoes = ctk.CTkFrame(aba_novocadastro, fg_color="transparent")
    linha_botoes.pack(pady=15)

    self.botao_salvar = ctk.CTkButton(
      linha_botoes,
      text="SALVAR",
      fg_color="green",
      hover_color="darkgreen"
    )
    self.botao_salvar.pack(side="left", padx=(0, 10))

    self.botao_cancelar = ctk.CTkButton(
      linha_botoes,
      text="CANCELAR",
      fg_color="gray60",
      hover_color="gray40",
      command=lambda: self.janela_abas.set("Login")
    )
    self.botao_cancelar.pack(side="left")


  
  # Aba Perfil
  def construir_perfil(self):

    aba_perfil = self.janela_abas.tab("Perfil")

    # Frame principal
    frame_principal = ctk.CTkFrame(aba_perfil, fg_color=PAPER)
    frame_principal.pack(fill="both", expand=True)

    # Menu lateral
    self.menu = ctk.CTkFrame(frame_principal, width=180, fg_color="#E8EAE8")
    self.menu.pack(side="left", fill="y", padx=(0, 10))
    self.menu.pack_propagate(False)

    # Titulo menu
    self.label_menu = ctk.CTkLabel(self.menu, text="MENU", font=("Arial", 18, "bold"))
    self.label_menu.pack(pady=20)

    # Botoes do menu
    self.btn_dashboard = ctk.CTkButton(self.menu, text="Dashboard", fg_color=GREEN)
    self.btn_dashboard.pack(padx=10, pady=5, fill="x")

    self.btn_oportunidades = ctk.CTkButton(self.menu, text="Oportunidades", fg_color=MINT)
    self.btn_oportunidades.pack(padx=10, pady=5, fill="x")

    self.btn_minhas_horas = ctk.CTkButton(self.menu, text="Minhas Horas", fg_color=MINT)
    self.btn_minhas_horas.pack(padx=10, pady=5, fill="x")

    self.btn_configuracoes = ctk.CTkButton(self.menu, text="Configurações", fg_color=MINT)
    self.btn_configuracoes.pack(padx=10, pady=5, fill="x")

    
    # Conteúdo central
    self.conteudo = ctk.CTkFrame(frame_principal, fg_color="transparent")
    self.conteudo.pack(side="left", fill="both", expand=True, padx=15, pady=15)

    # Título
    self.titulo_conteudo = ctk.CTkLabel(
      self.conteudo,
      text="MEU PERFIL - OLÁ, VOLUNTÁRIO",
      font=("Arial", 24, "bold"),
      text_color=INK
    )
    self.titulo_conteudo.pack(anchor="w", pady=(0, 20))

    # Cards
    self.frame_cards = ctk.CTkFrame(self.conteudo, fg_color="transparent")
    self.frame_cards.pack(fill="x", pady=(0, 20))

    # Card Status
    self.card_status = ctk.CTkFrame(self.frame_cards)
    self.card_status.pack(side="left", padx=5)

    self.label_titulo_status = ctk.CTkLabel(self.card_status,text="Status", font=("Arial", 14, "bold"))
    self.label_titulo_status.pack(padx=30, pady=(10, 5))

    self.label_conteudo_status = ctk.CTkLabel(
      self.card_status,
      text="Ativo",
      text_color=GREEN,
      font=("Arial", 24, "bold")
    )
    self.label_conteudo_status.pack(pady=(0, 10))

    # Card Horas
    self.card_horas = ctk.CTkFrame(self.frame_cards)
    self.card_horas.pack(side="left", padx=5)

    self.label_titulo_horas = ctk.CTkLabel(self.card_horas, text="Horas Doadas", font=("Arial", 14, "bold"))
    self.label_titulo_horas.pack(padx=30, pady=(10, 5))

    self.label_conteudo_horas = ctk.CTkLabel(
      self.card_horas,
      text="45h",
      text_color="#1F5A8A",
      font=("Arial", 24, "bold")
    )
    self.label_conteudo_horas.pack(pady=(0, 10))

    # Card Causas
    self.card_causas = ctk.CTkFrame(self.frame_cards)
    self.card_causas.pack(side="left", padx=5)

    self.label_titulo_causas = ctk.CTkLabel(
      self.card_causas,
      text="Causas",
      font=("Arial", 14, "bold")
    )
    self.label_titulo_causas.pack(padx=30, pady=(10, 5))

    self.label_conteudo_causas = ctk.CTkLabel(
      self.card_causas,
      text="Educação\nMeio Ambiente",
      justify="center"
    )
    self.label_conteudo_causas.pack(pady=(0, 10))

    
    # Oportunidades
    self.oportunidades = ctk.CTkFrame(self.conteudo)
    self.oportunidades.pack(fill="both", expand=True)

    self.label_titulo_oportunidades = ctk.CTkLabel(
      self.oportunidades,
      text="OPORTUNIDADES DISPONÍVEIS",
      font=("Arial", 18, "bold")
    )
    self.label_titulo_oportunidades.pack(anchor="w", padx=15, pady=15)

    # oportunidade 1
    self.card_op1 = ctk.CTkFrame(self.oportunidades)
    self.card_op1.pack(fill="x", padx=15, pady=5)

    self.label_op1 = ctk.CTkLabel(self.card_op1, text="Apoio em Evento Esportivo", font=("Arial", 14, "bold"))
    self.label_op1.pack(anchor="w", padx=10, pady=5)

    self.label_op1_conteudo = ctk.CTkLabel(self.card_op1, text="Comunicação • Meio Ambiente")
    self.label_op1_conteudo.pack(anchor="w", padx=10)

    self.btn_op1 = ctk.CTkButton(self.card_op1, text="Candidatar-se",fg_color=GREEN)
    self.btn_op1.pack(anchor="e", padx=10, pady=10)

    # oportunidade 2
    self.card_op2 = ctk.CTkFrame(self.oportunidades)
    self.card_op2.pack(fill="x", padx=15, pady=5)

    self.label_op2 = ctk.CTkLabel(self.card_op2, text="Monitoria para Crianças", font=("Arial", 14, "bold"))
    self.label_op2.pack(anchor="w", padx=10, pady=5)

    self.label_op2_conteudo = ctk.CTkLabel(self.card_op2, text="Educação • Crianças")
    self.label_op2_conteudo.pack(anchor="w", padx=10)

    self.btn_op2 = ctk.CTkButton(self.card_op2, text="Candidatar-se", fg_color=GREEN)
    self.btn_op2.pack(anchor="e", padx=10, pady=10)


  def entrar_perfil(self):
    # FUNÇÃO: é chamada quando o botão "Entrar" é clicado. Confere se o e-mail está no formato
    # correto (ex: fa@gmail.com) e se a senha tem pelo menos 6 caracteres.
    # Se estiver tudo certo, abre a aba "Perfil".

    email = self.campo_email.get()
    senha = self.campo_senha.get()

    # Formato do e-mail: texto + @ + texto + ponto + final com 2 ou mais letras (com, br, org...)
    formato_email = r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$"

    # 1ª verificação: campos vazios
    if not email or not senha:
      print("Preencha o email e a senha!")

    # 2ª verificação: o e-mail precisa seguir o formato acima
    elif not re.match(formato_email, email):
      print("Digite um email válido! Exemplo: nome@gmail.com")

    # 3ª verificação: a senha precisa ter pelo menos 6 caracteres
    elif len(senha) < 6:
      print("A senha deve ter no mínimo 6 caracteres!")

    # Se passou em tudo, troca para a aba "Perfil"
    else:
      self.janela_abas.set("Perfil")


  def criar_linha(self, pai):
    # Frame horizontal onde os campos ficam lado a lado
    linha = ctk.CTkFrame(pai, fg_color="transparent")
    linha.pack(fill="x", pady=5)
    return linha


  def criar_campo(self, pai, texto, placeholder, largura):
    # Cria uma coluna com label em cima e entry embaixo
    coluna = ctk.CTkFrame(pai, fg_color="transparent")
    coluna.pack(side="left", fill="x", expand =True, padx=(0, 20))

    label = ctk.CTkLabel(coluna, text=texto, font=("Arial", 14))
    label.pack(anchor="w", pady=(0, 5))

    entrada = ctk.CTkEntry(coluna, placeholder_text= placeholder, width= largura)
    entrada.pack(fill="x")

    return entrada

    

janela = Aplicativo()
janela.mainloop()