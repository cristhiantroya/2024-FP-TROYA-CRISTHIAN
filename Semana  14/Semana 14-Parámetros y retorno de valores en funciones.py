def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado al monto total de la compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

if __name__ == "__main__":
    # Primer caso: monto total con descuento predeterminado
    monto1 = 200.00  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1

    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f} (10%)")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segundo caso: monto total con un porcentaje de descuento específico
    monto2 = 150.00  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento específico
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2

    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f} ({porcentaje2}%)")
    print(f"Monto final a pagar: ${monto_final2:.2f}")