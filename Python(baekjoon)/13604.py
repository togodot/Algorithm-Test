### 13604번: Jogo de Estratégia

# 문제
# Um jogo de estratégia, com J jogadores, é jogado em volta de uma mesa. O primeiro a jogar é o jogador 1, o segundo a jogar é o jogador 2 e assim por diante. Uma vez completada uma rodada, novamente o jogador 1 faz sua jogada e a ordem dos jogadores se repete novamente. A cada jogada, um jogador garante uma certa quantidade de Pontos de Vitória. A pontuação de cada jogador consiste na soma dos Pontos de Vitória de cada uma das suas jogadas.
# 
# Dado o número de jogadores, o número de rodadas e uma lista representando os Pontos de Vitória na ordem em que foram obtidos, você deve determinar qual é o jogador vencedor. Caso mais de um jogador obtenha a pontuação máxima, o jogador com pontuação máxima que tiver jogado por último é o vencedor.
# 
# 입력
# A entrada consiste de duas linhas. A primeira linha contém dois inteiros J e R, o número de jogadores e de rodadas respectivamente (1 ≤ J, R ≤ 500). A segunda linha contém J × R inteiros, correspondentes aos Pontos de Vitória em cada uma das jogadas feitas, na ordem em que aconteceram. Os Pontos de Vitória obtidos em cada jogada serão sempre inteiros entre 0 e 100, inclusive.
# 
# 출력
# Seu programa deve produzir uma única linha, contendo o inteiro correspondente ao jogador vencedor.

J, R = map(int, input().split())
score_list = list(map(int, input().split()))
score_sum_list = []

for i in range(J):     #플레이어 수 만큼 반복
    for j in range(R):       # 라운드 수 만큼 반복
        if j == 0:
            score = score_list[i]
        else:
            score += score_list[i+(j*J)]
    score_sum_list.append(score)

max_score = max(score_sum_list)

for i, e in reversed(list(enumerate(score_sum_list))):
    if e == max_score:
        answer = i + 1
        break
print(answer)
