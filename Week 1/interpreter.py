def main ():

    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    #print (x,y,z)
    x = float(x)
    z = float(z)
    print(interpreter(x,y,z))


def interpreter(i,j,k):

    match j:
        case "+":
            return float(i+k)
        case "-":
            return float(i-k)
        case "*":
            return float(i*k)
        case "/":
            return float(i/k)

main()
