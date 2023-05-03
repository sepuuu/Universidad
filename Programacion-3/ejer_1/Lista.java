
public class Lista {
    public Nodo primero;
    public Nodo ultimo;
    
    public Lista() {
        primero = null;
        ultimo  = null;
    }
    
    public void insertarPorDelante(Nodo nuevo) {
    if (primero == null) {
        primero = nuevo;
        ultimo = nuevo;
    } else {
        
        nuevo.siguiente = primero;
        primero.anterior = nuevo;
        primero = nuevo;
    }
    }

    public void insertarPorAtras(Nodo nuevo) {
        //##
        //##
        //##
    }
   
    
    public void invertir() {
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
    }
    
    
    public void insertarEnOrden(Nodo nuevo) {
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
        //##
    }
    
    
    public void mostrar() {
        System.out.print("Lista =");
        if(primero==null) System.out.println("vacia");
        else {
            Nodo este = primero;
            while(este!=null) {
                System.out.print("  " + este.info);
                este = este.nexo;
            }
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Lista lista1 = new Lista();
        Lista lista2 = new Lista();
        Lista lista3 = new Lista();
        
        Nodo  nuevoNodo;
        
        int N   = 10 + (int)(Math.random()*10);
        int M[] = new int[N];
        System.out.print("Arreglo con valores al azar   M[]   =");
        for(int i=0;i<N;i++) {
            M[i] = 10 + (int)(Math.random()*90);
            System.out.print("  " + M[i]);
        }
        System.out.println("\n");
        

        for(int i=0;i<N;i++) {
            nuevoNodo = new Nodo(M[i]);
            lista1.insertarPorDelante(nuevoNodo);
            
            nuevoNodo = new Nodo(M[i]);
            lista2.insertarPorAtras(nuevoNodo);
            
            nuevoNodo = new Nodo(M[i]);
            lista3.insertarEnOrden(nuevoNodo);
        }

        System.out.print("Nodos insertados por delante  "); lista1.mostrar();
        lista1.invertir();
        System.out.print("Esta  misma  lista invertida  "); lista1.mostrar();
        System.out.println();
        
        System.out.print("Nodos insertados  por detras  "); lista2.mostrar();
        System.out.println();
        
        System.out.print("Nodos  insertados  en  orden  "); lista3.mostrar();
        System.out.println();        
    }
}

class Nodo {
    int  info;
    Nodo nexo;
    Nodo siguiente;
    Nodo anterior;
    
    public Nodo(int dato) {
        this.info = dato;
        this.nexo = null;
        this.siguiente=null;
        this.anterior=null;
    }
}