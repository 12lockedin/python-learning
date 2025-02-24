**%**
Con el operador de módulo podemos obtener el resto de la división.

Normalmente **se utiliza para saber si un número es divisible entre otro**. 
	¿Por qué?
		Porque si un número es divisible entre otro, el resto es 0.
			Por ejemplo, todos los números pares, son divisibles entre 2, por lo que:
			numero par % 2 dará 0 siempre

Por lo que si hacemos el resto de la división entre 10, tendremos siempre las unidades de ese número:

```python
num % 10

# Siempre nos dará las unidades de ese número.
24 % 10
4
```

### Explanation:
1. **Modulo Operator (`%`)**: The modulo operator (`% 10`) is used to determine the last digit of the number. This helps identify numbers ending with `1`, `2`, or `3`.
2. Podemos utilizarlo para quitar las unidades, decenas, centenas: % entre 10, 100, 1000...
