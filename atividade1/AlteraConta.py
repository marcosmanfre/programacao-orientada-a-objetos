from ContaCorrente import ContaCorrente 

conta1 = ContaCorrente("Marcos", "376.981.644-05", "Bradesco", "15-0", "15555-4", 500, 5000)
print(conta1)

conta2 = ContaCorrente("Arthur", "371.648.222-02", "Santander", "165-5", "165755-2", 2000, 5000)
print(conta2)


conta1.setNome('Baltazar')
print(conta1.getNome())
print(conta1)

conta1.extrato()

conta2.extrato()

conta1.deposita(500)
conta1.extrato()
conta1.saca(800)
conta1.extrato

conta2.saca(500)
conta2.extrato()
conta2.deposita(1000)
conta2.extrato()