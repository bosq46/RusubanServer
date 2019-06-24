#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

int SW_PIN[] = {7, 0, 2};  //TODO:ボタンのピンの確認・ボタンは３つ
int SW_FLG[] = {0, 0, 0};
char *btn0_cmd = "python3 -V";  //とりあえずPythonを呼び出せるか確認
char *btn1_cmd = "python2 -V";
char *btn2_cmd = "gcc --version";
int res;


int main(int argc, char *argv[]) {
    if (wiringPiSetup() == -1) {
        printf("Error: setup failed.\n");
        return -1;
    }

    pinMode(SW_PIN[0], INPUT);
    pinMode(SW_PIN[1], INPUT);
    pinMode(SW_PIN[2], INPUT);

    pullUpDnControl(SW_PIN[0], PUD_DOWN);
    pullUpDnControl(SW_PIN[1], PUD_DOWN);
    pullUpDnControl(SW_PIN[2], PUD_DOWN);

    printf("PIN{0]: %d\n", digitalRead(SW_PIN[0]));
    printf("PIN[1]: %d\n", digitalRead(SW_PIN[1]));
    printf("PIN[2]: %d\n", digitalRead(SW_PIN[2]));

    while(1) {
        //TODO:チャタリング除去
        //現在はフラグで複数回押されてもbtn*_cmd()関数を実行しないように実装しているが
        //チャタリングのため複数回実行されるようになっている．
        //そのためチャタリング除去が必要！！！！
        //******実装方法*******
        // 1. SW_FLG（フラグ）でなく, 押した時の時間を取得し保存
        // 2. ボタン押下時に, 保存した時刻からN秒経過しているか確認
        // 3. 経過していればbtn*_cmd()を実行
        /* btn0 */
        if (SW_FLG[0] == 0 && digitalRead(SW_PIN[0]) == 1 ) {
            delay(5);
            if (digitalRead(SW_PIN[0]) == 1 ) {
                printf("SW:0 is ON\n");
                SW_FLG[0] = 1;

                printf("------------------------------------\n");
                res = system(btn0_cmd);
                printf("------------------------------------\n");
                printf("%d\n", WIFEXITED(res));
                delay(1000);
            }
        } else if(SW_FLG[0] == 1 && digitalRead(SW_PIN[0]) == 0) {
            printf("SW:0 is OFF\n");
            SW_FLG[0] = 0;
        }

        /* btn1 */
        if (SW_FLG[1] == 0 && digitalRead(SW_PIN[1]) == 1 ) {
            delay(5);
            if (digitalRead(SW_PIN[1]) == 1 ) {
                printf("SW:1 is ON\n");
                SW_FLG[1] = 1;

                printf("------------------------------------\n");
                res = system(btn1_cmd);
                printf("------------------------------------\n");
                printf("%d\n", WIFEXITED(res));
                delay(1000);
            }
        } else if(SW_FLG[1] == 1 && digitalRead(SW_PIN[1]) == 0) {
            printf("SW:1 is OFF\n");
            SW_FLG[1] = 0;
        }

        /* btn2 */
        if (SW_FLG[2] == 0 && digitalRead(SW_PIN[2]) == 1 ) {
            delay(5);
            if (digitalRead(SW_PIN[2]) == 1 ) {
                printf("SW:2 is ON\n");
                SW_FLG[2] = 1;

                printf("------------------------------------\n");
                res = system(btn2_cmd);
                printf("------------------------------------\n");
                printf("%d\n", WIFEXITED(res));
                delay(1000);
            }
        } else if(SW_FLG[2] == 1 && digitalRead(SW_PIN[2]) == 0) {
            printf("SW:2 is OFF\n");
            SW_FLG[2] = 0;
        }
    }
    return 0;
}
