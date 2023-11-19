package Animais;

public class Gato extends Animal {

    static int numeroGatos;

    public Gato(String nome, String cor, int altura, double peso) {
        super(nome, cor, altura, peso);
        numeroGatos ++;
    }

    @Override
    public void soar() {
        System.out.println("miau miau");
    }

    @Override
    protected void comer() {
      System.out.println("peixe");
    }

    @Override
    protected void dormir() {
        System.out.println("sofá");;
    }
   
}
