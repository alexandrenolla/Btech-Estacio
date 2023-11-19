import Animais.Animal;
import Animais.Cachorro;
import Animais.Gato;
import Animais.Passaro;
import Petshop.Petshop;

public class Main {
    public static void main(String[] args) {

        System.out.println(Cachorro.getNumeroCachorros());

        Cachorro cachorro1 = new Cachorro("Eros", "Branco e Preto", 30, 15.5);

        Gato gato1 = new Gato("Cherry", "Caramelo", 15, 5.0);

        Animal passaro1 = new Passaro("Stuart", "Azul", 10, 2);

        cachorro1.soar();
        gato1.soar();
        passaro1.soar();

        System.out.println("O cachorro pegou uma " + cachorro1.pegar());

        System.out.println("O cachorro está " + cachorro1.interagir("carinho"));
        System.out.println("O cachorro está " + cachorro1.interagir("nada"));
        System.out.println("O cachorro está " + cachorro1.interagir("vai dormir"));

        System.out.println(cachorro1.getNome());
        System.out.println(cachorro1.getPeso());

        System.out.println(passaro1.getNome());


        Petshop petshop = new Petshop();

        petshop.darBanho(passaro1);
        System.out.println(passaro1.getEstadoEspirito());

        petshop.darBanho(gato1);
        System.out.println(gato1.getEstadoEspirito());

        petshop.tosar(cachorro1);
        System.out.println(cachorro1.getEstadoEspirito());
    }
}
