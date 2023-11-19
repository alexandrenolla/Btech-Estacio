package Animais;

public class Passaro extends Animal {
    
    static int numeroPassaros;

    public Passaro(String nome, String cor, int altura, double peso) {
        super(nome, cor, altura, peso);
        numeroPassaros ++;
    }

    @Override
    public void soar() {
        System.out.println("prr prr");
    }

    @Override
    protected void comer() {
        System.out.println("semente");
    }

    @Override
    protected void dormir() {
       System.out.println("árvore");
    }
}
