package Petshop;

import Animais.Animal;
import Animais.Cachorro;

public class Petshop {
    
    public void darBanho(Animal animal) {
        animal.setEstadoEspirito("Limpo");
    }

    public void tosar(Cachorro cachorro) {
        cachorro.setEstadoEspirito("Tosado");
    }

    public void deixarNoHotel(Animal animal) {
        animal.setEstadoEspirito("com saudades");
    }
}

