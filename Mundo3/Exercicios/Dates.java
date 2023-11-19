import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.TextStyle;
import java.util.Locale;

public class Dates {
    public static void main(String[] args) {
		
		//Horário
		ZoneId brasilHora = ZoneId.of("America/Sao_Paulo");
		LocalDateTime horario = LocalDateTime.now(brasilHora);
		
		//Dia
		LocalDate data = LocalDate.now();
		Locale brasilData = new Locale("pt","BR");
		String diaSemana = data.getDayOfWeek().getDisplayName(TextStyle.FULL, brasilData);
		Integer diaMes = data.getDayOfMonth();
		Integer ano = data.getYear();
		
		// Mês
		String mes = data.getMonth().getDisplayName(TextStyle.FULL, brasilData);

		String nome = "Alexandre";
		String saudacao;
		String artigo;

		if (horario.getHour() >= 0 && horario.getHour() < 6) {
			saudacao = "Boa madrugada";
			artigo = "uma";
		} else if (horario.getHour() >= 6 && horario.getHour() < 13) {
			saudacao = "Bom dia";
			artigo = "um";
		} else if (horario.getHour() >= 13 && horario.getHour() < 19) {
			saudacao = "Boa tarde";
			artigo = "uma";
		} else {
			saudacao = "Boa noite";
			artigo = "uma";
		}
		
		// Imprime o horário sem os milisegundos e sem a data, usando um formato personalizado
		System.out.printf("Olá, %s! Hoje é %s, %d de %s de %d.\nAgora são %s.\nTenha %s %s!", nome, diaSemana, diaMes, mes, ano, horario.format(DateTimeFormatter.ofPattern("HH:mm:ss")), artigo, saudacao.toLowerCase());
	
	}
}
