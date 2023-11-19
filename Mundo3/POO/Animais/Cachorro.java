package Animais;

public class Cachorro extends Animal{
    //1. ATRIBUTOS
    static int numeroCachorros;

    //2. CONSTRUTORES
    public Cachorro(String nome, String cor, int altura, double peso) {
        super(nome, cor, altura, peso);
        numeroCachorros++;
    }

    //3. MÉTODOS
    public static int getNumeroCachorros() {
        return numeroCachorros;
    }
    
    public String pegar() {
        return "bolinha";
    }

    @Override
    public void soar() {
        System.out.println("au au");
    }

    @Override
    protected void comer() {
        System.out.println("carne");
    }

    @Override
    protected void dormir() {
        System.out.println("cama");
    }

}