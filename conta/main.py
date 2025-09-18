# No arquivo main.py
from datetime import date
from PessoaFisica import PessoaFisica
from ContaCorrente import ContaCorrente
from Transacao import Deposito, Saque

# 1. Criando um cliente (mesmo de antes)
cliente1 = PessoaFisica(
    nome="Maria Oliveira",
    cpf="987.654.321-00",
    data_nascimento=date(1985, 5, 20),
    endereco="Avenida B, 456"
)
print(f"Cliente '{cliente1.nome}' criado.")

# 2. Criando uma CONTA CORRENTE para o cliente
# Passamos o número, o cliente, um limite de R$ 500 e um limite de 3 saques.
conta_corrente = ContaCorrente(numero=101, cliente=cliente1, limite=500.0, limite_saques=3)
print(f"Conta Corrente número {conta_corrente._numero} criada para {cliente1.nome} com limite de R$ {conta_corrente._limite:.2f}.")

# 3. Realizando transações para testar as novas regras
print("\n--- Realizando Transações na Conta Corrente ---")

# Depósito inicial
Deposito(1000.00).registrar(conta_corrente) # Saldo: 1000

# Saque normal (1º saque do dia)
Saque(200.00).registrar(conta_corrente) # Saldo: 800

# Saque usando o limite/cheque especial (2º saque do dia)
Saque(1000.00).registrar(conta_corrente) # Saldo: -200

# Saque normal (3º saque do dia)
Saque(100.00).registrar(conta_corrente) # Saldo: -300

# Tentativa de 4º saque (deve falhar pelo limite de saques)
print("\n--- Testando Limite de Quantidade de Saques ---")
Saque(50.00).registrar(conta_corrente)

# Tentativa de saque maior que o saldo+limite (deve falhar)
print("\n--- Testando Limite de Crédito ---")
Saque(300.00).registrar(conta_corrente) # Saldo é -300, limite é 500. Disponível: 200. Saque de 300 falha.

# 4. Verificando o saldo final
print(f"\nSaldo final da conta: R$ {conta_corrente.saldo:.2f}")