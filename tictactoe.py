# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# Importing standard Qiskit libraries and configuring account
import qiskit
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
# from qiskit.visualization import *
# Loading your IBM Q account(s)
# provider = IBMQ.load_account()

def winner(game):
    if(game[0]==1 and game[1]==1 and game[2]==1):
        print("winner : player 1")
        return 1
    elif(game[3]==1 and game[4]==1 and game[5]==1):
        print("winner : player 1")
        return 1
    elif(game[6]==1 and game[7]==1 and game[8]==1):
        print("winner : player 1")
        return 1
    elif(game[0]==1 and game[3]==1 and game[6]==1):
        print("winner : player 1")
        return 1
    elif(game[1]==1 and game[4]==1 and game[7]==1):
        print("winner : player 1")
        return 1
    elif(game[2]==1 and game[5]==1 and game[8]==1):
        print("winner : player 1")
        return 1    
    elif(game[0]==1 and game[4]==1 and game[8]==1):
        print("winner : player 1")
        return 1
    elif(game[2]==1 and game[4]==1 and game[6]==1):
        print("winner : player 1")
        return 1
    elif(game[0]==2 and game[1]==2 and game[2]==2):
        print("winner : player 2")
        return 1
    elif(game[3]==2 and game[4]==2 and game[5]==2):
        print("winner : player 2")
        return 1
    elif(game[6]==2 and game[7]==2 and game[8]==2):
        print("winner : player 2")
        return 1
    elif(game[0]==2 and game[3]==2 and game[6]==2):
        print("winner : player 2")
        return 1
    elif(game[1]==2 and game[4]==2 and game[7]==2):
        print("winner : player 2")
        return 1
    elif(game[2]==2 and game[5]==2 and game[9]==2):
        print("winner : player 2")
        return 1    
    elif(game[0]==2 and game[4]==2 and game[8]==2):
        print("winner : player 2")
        return 1
    elif(game[2]==2 and game[4]==2 and game[6]==2):
        print("winner : player 2")
        return 1
    return 0

def choice(a,b):
    q=qiskit.QuantumRegister(9)
    c=qiskit.ClassicalRegister(9)
    circuit=QuantumCircuit(q,c)

    circuit.x(a)
    circuit.h(b)
    circuit.cx(b,a)
    circuit.measure([0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8])

    backend = Aer.get_backend('qasm_simulator')
    mapped_circuit = transpile(circuit, backend=backend)
    result = execute(mapped_circuit, backend=backend, shots=1).result()
    count= result.get_counts()
    a=(list(count))
    return a[0]

print("reffer the following for position")
for i in range(9):
    if(i%3==0):
        print("\n")
    print(i,end="|")
win=0
game=[0]*(9)
activeplayer=1
print("player 1")
while(1):
    if(activeplayer==1):
        print("enter the position you want to play")
        a=int(input())
        b=int(input())
        if(game[a]!=0 or game[b]!=0 or a==b):
            print("invalid input enter again(either both input are same or occupied place selected)",end="\n")
            a=int(input())
            b=int(input())
            if(game[a]!=0 or game[b]!=0 or a==b):
                print("Am i a joke to you",end="\n")
                a=int(input())
                b=int(input())
        c=choice(int(a),int(b))
        for i in range(len(c)):
            if(c[len(c)-1-i]=='1' and game[i]==0):
                game[i]=1            
        activeplayer=2
        for i in range(len(game)):
            if(i%3==0):
                print("\n")
            print(game[i],end="|")
        print("\n")
        print("player 2")
        win=winner(game)
    if(activeplayer==2):
        print("enter position you want to play")
        a=int(input())
        b=int(input())
        if(game[a]!=0 or game[b]!=0 or a==b):
            print("invalid input enter again(either both input are same or occupied place selected)",end="\n")
            a=int(input())
            b=int(input())
            if(game[a]!=0 or game[b]!=0 or a==b):
                print("Am i a joke to you",end="\n")
                a=int(input())
                b=int(input())
        c=choice(int(a),int(b))
        for i in range(len(c)):
            if(c[len(c)-1-i]=='1' and game[i]==0):
                game[i]=2
        activeplayer=1
        for i in range(len(game)):
            if(i%3==0):
                print("\n")
            print(game[i],end="|")
        print("\n")
        print("player 1")
        win=winner(game)
    for i in range(len(game)):
        if(i%3==0):
            print("\n")
        print(game[i],end="|")
    if(win==1):
        break
    if(sum(game)==13 and win==0):
        print("draw")
        break









