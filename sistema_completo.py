
import customtkinter as ctk


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro de Voluntarios")
        self.geometry("900x600")

        # Permite que a linha e a coluna ocupem o espaço disponível
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Janela de abas
        self.janela_abas = ctk.CTkTabview(self, width=600)
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



        # Título do login
        self.titulo_login = ctk.CTkLabel(aba_login,
                                         text = "Bem-Vindo ao Portal de Voluntarios",
                                           font = ("Arial", 20, "bold"),
                                           width = 300)
        self.titulo_login.pack(pady = (40, 30))


        # Campo de email
        self.label_email = ctk.CTkLabel(
        aba_login,
        text="E-mail",
        font=("Arial", 16)
        )
        self.label_email.pack(pady=(10, 5), padx=(10, 100))

        
        # Campo de entrada para o email
        self.campo_email = ctk.CTkEntry(aba_login,
                                    placeholder_text="Digite seu email")
        self.campo_email.pack(pady=(5, 10), padx=20)


        # Campo de senha
        self.label_senha = ctk.CTkLabel(aba_login,
                                        text="Senha",
                                        font=("Arial", 16))
        self.label_senha.pack(pady=(5, 5), padx=(10, 100))


        # Campo de entrada para a senha
        self.campo_senha = ctk.CTkEntry(aba_login,
                                    placeholder_text="Digite sua senha",
                                    show="*")
        self.campo_senha.pack(pady=(5, 10), padx=20)


        # Botão de entrar
        self.botao_entrar = ctk.CTkButton(aba_login,
                                          text="Entrar",
                                          fg_color = "green",
                                          hover_color = "darkgreen",
                                          command = self.entrar_perfil)

        self.botao_entrar.pack(pady=(5, 10), padx=20)


        # Campo de cadastro
        self.campo_cadastro = ctk.CTkButton(
                                    aba_login,
                                    text="Não tem uma conta? Cadastre-se",
                                    fg_color="transparent",
                                    text_color="blue",
                                    hover=False,
                                    command=lambda: self.janela_abas.set("Novo Cadastro")
                                    )

        self.campo_cadastro.pack(pady=(5, 10))



    def construir_novocadastro(self):

        #Criando a aba de novo cadastro
        aba_novocadastro = self.janela_abas.tab("Novo Cadastro")


        # Título do cadastro
        self.titulo_cadastro = ctk.CTkLabel(aba_novocadastro,
                                            text = "Novo cadastro de voluntário",
                                            font = ("Arial", 20, "bold",)
                                            )
        self.titulo_cadastro.pack(anchor="nw", padx =10, pady=10)


        # Seção de Dados Pessoais
        self.dados_pessoais = ctk.CTkLabel(aba_novocadastro,
                                           text = "Dados Pessoais",
                                            font = ("Arial", 16, "bold"))
        self.dados_pessoais.pack(anchor="nw", padx =10, pady=10)
        

                # Linha com Nome Completo e CPF lado a lado
        linha_nome_cpf = self.criar_linha(aba_novocadastro)
        linha_nome_cpf.pack_configure(padx=10)

        self.campo_nome = self.criar_campo(linha_nome_cpf,
                                           "Nome Completo",
                                           "Digite seu nome completo",
                                           400)

        self.campo_cpf_entrada = self.criar_campo(linha_nome_cpf,
                                                  "CPF",
                                                  "Digite seu CPF",
                                                  200)

                # Linha com Data de Nascimento e Gênero
        linha_nascimento_genero = self.criar_linha(aba_novocadastro)
        linha_nascimento_genero.pack_configure(padx=10)

        self.campo_nascimento = self.criar_campo(linha_nascimento_genero,
                                                 "Data de Nascimento",
                                                 "DD/MM/AAAA",
                                                 200)

        # Gênero é uma lista de opções (ComboBox), então é montado à mão
        coluna_genero = ctk.CTkFrame(linha_nascimento_genero, fg_color="transparent")
        coluna_genero.pack(side="left", padx=(0, 20))

        self.label_genero = ctk.CTkLabel(coluna_genero, text="Gênero", font=("Arial", 14))
        self.label_genero.pack(anchor="w", pady=(0, 5))

        self.campo_genero = ctk.CTkComboBox(coluna_genero,
                                            values=["Feminino", "Masculino", "Outro", "Prefiro não informar"],
                                            width=200)
        self.campo_genero.set("Selecione")
        self.campo_genero.pack(anchor="w")


        # Seção de Contato
        self.contato = ctk.CTkLabel(aba_novocadastro,
                                    text="Contato",
                                    font=("Arial", 16, "bold"))
        self.contato.pack(anchor="nw", padx=10, pady=10)


        # Linha com E-mail e Telefone
        linha_email_telefone = self.criar_linha(aba_novocadastro)
        linha_email_telefone.pack_configure(padx=10)

        self.campo_email_cadastro = self.criar_campo(linha_email_telefone,
                                                     "E-mail",
                                                     "Digite seu e-mail",
                                                     300)

        self.campo_telefone = self.criar_campo(linha_email_telefone,
                                               "Telefone",
                                               "(00) 00000-0000",
                                               200)


        # Linha com Endereço (sozinho)
        linha_endereco = self.criar_linha(aba_novocadastro)
        linha_endereco.pack_configure(padx=10)

        self.campo_endereco = self.criar_campo(linha_endereco,
                                               "Endereço Completo",
                                               "Rua, número, bairro, cidade",
                                               520)


        # Seção de Perfil
        self.perfil = ctk.CTkLabel(aba_novocadastro,
                                   text="Perfil",
                                   font=("Arial", 16, "bold"))
        self.perfil.pack(anchor="nw", padx=10, pady=10)


        # Interesses/Causas
        linha_interesses = self.criar_linha(aba_novocadastro)
        linha_interesses.pack_configure(padx=10)
        self.campo_interesses = self.criar_campo(linha_interesses,
                                                 "Interesses/Causas",
                                                 "Ex: Educação, Meio Ambiente",
                                                 520)

        # Habilidades
        linha_habilidades = self.criar_linha(aba_novocadastro)
        linha_habilidades.pack_configure(padx=10)
        self.campo_habilidades = self.criar_campo(linha_habilidades,
                                                  "Habilidades",
                                                  "Ex: Comunicação, Informática",
                                                  520)

        # Disponibilidade
        linha_disponibilidade = self.criar_linha(aba_novocadastro)
        linha_disponibilidade.pack_configure(padx=10)
        self.campo_disponibilidade = self.criar_campo(linha_disponibilidade,
                                                      "Disponibilidade [dias/horários]",
                                                      "Ex: Sábados, manhã",
                                                      520)


        # Botões Salvar e Cancelar lado a lado
        linha_botoes = ctk.CTkFrame(aba_novocadastro, fg_color="transparent")
        linha_botoes.pack(anchor="nw", padx=10, pady=15)

        self.botao_salvar = ctk.CTkButton(linha_botoes,
                                          text="SALVAR",
                                          fg_color="green",
                                          hover_color="darkgreen")
        self.botao_salvar.pack(side="left", padx=(0, 10))

        self.botao_cancelar = ctk.CTkButton(linha_botoes,
                                            text="CANCELAR",
                                            fg_color="gray60",
                                            hover_color="gray40",
                                            command=lambda: self.janela_abas.set("Login"))
        self.botao_cancelar.pack(side="left")





    def construir_perfil(self):
        pass

    def entrar_perfil(self):

        email = self.campo_email.get()
        senha = self.campo_senha.get()

        if not email or not senha:
            print("Preencha o email e a senha!")

        elif "@" not in email or "." not in email.split("@")[-1]:
            print("Digite um email válido!")

        else:
            self.janela_abas.set("Perfil")


    def criar_linha(self, pai):
        # Frame horizontal onde os campos ficam lado a lado
        linha = ctk.CTkFrame(pai, fg_color="transparent")
        linha.pack(anchor="nw", pady=5)
        return linha


    def criar_campo(self, pai, texto, placeholder, largura):
        # Cria uma coluna com label em cima e entry embaixo
        coluna = ctk.CTkFrame(pai, fg_color="transparent")
        coluna.pack(side="left", padx=(0, 20))

        label = ctk.CTkLabel(coluna, text=texto, font=("Arial", 14))
        label.pack(anchor="w", pady=(0, 5))

        entrada = ctk.CTkEntry(coluna, placeholder_text=placeholder, width=largura)
        entrada.pack(anchor="w")

        return entrada

    

janela = Aplicativo()
janela.mainloop()