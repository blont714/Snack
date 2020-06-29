import random
import time
import copy


SHORTCUT_LIST = ['Windows', 'Windows + D', 'Windows + S', 'Windows + I', 'Windows + A',
                 'Windows + W', 'Windows + 1～0', 'Alt + Tab', 'Windows + Tab', 'Windows + Ctrl + D',
                 'Windows + Ctrl + ←→', 'Windows + Ctrl + F4', 'Ctrl + Z', 'Ctrl + Y', 'Ctrl + A',
                 'Shift + ↑↓←→', 'Ctrl + X', 'Ctrl + C', 'Ctrl + V', 'Windows + V',
                 'Ctrl + N', 'Ctrl + S', 'Ctrl + O', 'Ctrl + P', 'Shift + F10',
                 'Windows + E', 'Ctrl + Shift + 1～8', 'Alt + ←', 'Alt + →', 'Alt + ↑',
                 'F2', 'Ctrl + Shift + N', 'Ctrl + F', 'Ctrl + F1', 'Ctrl + ↑↓←→ ⇒ Space',
                 'Shift + Delete', 'Alt + F4', 'Alt + Enter', 'Alt + P', 'F4',
                 'Alt + Space', 'Windows + ↑↓', 'Windows + ←→', 'Windows + M', 'Ctrl + W',
                 'Windows + P', 'PrintScreen', 'Windows + PrintScreen', 'Windows + Shift + S', 'Windows + R',
                 'Ctrl + Shift + Esc', 'Windows + L', 'Windows + X']
ANSWER_LIST = ['1:スタートメニューを表示', '2:デスクトップを表示', '3:Cortanaを起動', '4:設定画面を表示', '5:アクションセンターを表示',
               '6:Windows Ink Workspaceを起動', '7:タスクバーからアプリを起動', '8:アプリやウィンドウを切り替え', '9:タスクビューを表示', '10:仮想デスクトップを追加',
               '11:仮想デスクトップを切り替え', '12:仮想デスクトップを閉じる', '13:操作を元に戻す', '14:元に戻した操作をやり直す', '15:すべての項目を選択',
               '16:複数項目を選択', '17:選択した項目を切り取る', '18:選択した項目をコピーする', '19:切り取り、コピーした項目を貼り付ける', '20:クリップボードの履歴表示',
               '21:新規ウィンドウを開く/ファイルを作成する', '22:ファイルを保存', '23:ファイルを開く', '24:ファイルを印刷する', '25:ショートカットメニュー表示',
               '26:エクスプローラー起動', '27:アイコンの表示形式変更', '28:前のフォルダに戻る', '29:戻る前のフォルダに進む', '30:親フォルダに移動',
               '31:ファイルやフォルダの名前変更', '32:新しいフォルダの作成', '33:ファイルやフォルダを検索', '34:リボンを表示', '35:離れている複数項目選択',
               '36:ファイルやフォルダを完全削除', '37:ウィンドウを閉じる', '38:プロパティを表示', '39:プレビューパネルを表示', '40:アドレスバーに履歴を表示',
               '41:ウィンドウのメニューを表示', '42:ウィンドウを最大化・最小化', '43:ウィンドウを左半分・右半分に合わせる', '44:すべてのウィンドウを最小化', '45:ウィンドウを閉じる',
               '46:画面の表示モードを選択', '47:スクリーンショット撮影', '48:スクリーンショット撮影＆保存', '49:指定範囲のスクリーンショット撮影', '50:[ファイル名を指定して実行]を表示',
               '51:[タスクマネージャー]を表示する', '52:パソコンをロックする', '53:クイックリンクメニューを表示する']
answer_list = copy.deepcopy(ANSWER_LIST)

def make_question_number_list(num):
    ns = list(range(num))
    random.shuffle(ns)
    return ns

def question(num):
    global correct, wrong
    print()
    print('残り'+str(questions-i)+'問')
    print()
    print(SHORTCUT_LIST[num])
    print()
    for j in range(questions):
        if (j+1)%5!=0:
            print(answer_list[j].center(20), end='')
        else:
            print(answer_list[j].center(20))
            print()
    print()
    A = int(input())
    if A == num + 1:
        print('正解')
        correct += 1
    else:
        print('不正解 正解は'+ANSWER_LIST[num])
        wrong += 1

    time.sleep(2)
    print('------------------------------------')
    return

if __name__ == '__main__':
    correct = 0
    wrong = 0
    questions = len(SHORTCUT_LIST)
    question_number_list = make_question_number_list(questions)
    for i in range(questions):
        question(question_number_list[i])
        answer_list[question_number_list[i]] = ''
    print('終了 '+str(correct)+'問正解、'+str(wrong)+'問不正解')
