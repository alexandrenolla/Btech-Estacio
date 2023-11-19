package Animais;

public abstract class Animal {
    // 1. PROPRIEDADES
    protected String nome;
    protected String cor;
    protected int altura;
    protected double peso;
    protected String estadoEspirito;

    // 2. CONSTRUTORES
    public Animal(String nome, String cor, int altura, double peso) {
        this.nome = nome;
        this.cor = cor;
        this.altura = altura;
        this.peso = peso;
    }
    // 3. MÉTODOS
    protected abstract void comer();

    protected abstract void dormir();

    public abstract void soar();

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCor() {
        return this.cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getAltura() {
        return this.altura;
    }

    public void setAltura(int altura) {
        this.altura = altura;
    }

    public double getPeso() {
        return this.peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public String getEstadoEspirito() {
        return this.estadoEspirito;
    }
    public void setEstadoEspirito(String estadoEspirito) {
        this.estadoEspirito = estadoEspirito; 
    }

    public String interagir(String acao) {
        switch(acao) {
            case "carinho": this.estadoEspirito = "feliz"; break;
            case "vai dormir": this.estadoEspirito = "chateado"; break;
            case "nada": this.estadoEspirito = "neutro"; break;
            default: this.estadoEspirito = "neutro"; break;
        }
        // if (acao.equals("carinho")) {
        //     this.estadoEspirito = "feliz";
        // }else if (acao.equals("vai dormir")){
        //     this.estadoEspirito = "chateado";
        // } else {
        //     this.estadoEspirito = "neutro";
        // }
        return this.estadoEspirito;
    }
}
