#include <windows.h>
#include <commctrl.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <mmsystem.h>
#include "Resource.h"

//x86_64-w64-mingw32-gcc main.c -o app.exe -Wall -mwindows -lcomctl32 -lwinmm

const char szClassName[] = "myWindowClass";
HINSTANCE hInst;
HWND sButton, hLabel, hCounter, addButton, subButton, rButton,  myWnd;
HBITMAP hBitmap;

long int start, lastSeconds;
long int settingTimer = 60;

BOOL FlagStop = FALSE;
BOOL FlagRetry = TRUE;
BOOL FlagContinue = FALSE;

TCHAR buffer[64];

void ParseTimeToString(long int seconds) 
{
	if (seconds < 60) {
		sprintf(buffer, "%ld", seconds);
	} else if (seconds < 60 * 60) {
		sprintf(buffer, "%ld:%ld", seconds / 60, seconds % 60);
	}
	else {
		sprintf(buffer, "%ld:%ld:%ld", seconds / (60 * 60), (seconds % (60 * 60)) / 60, seconds % 60);
	}
}

BOOL CALLBACK EnumDesktopWindowsProc(HWND hwnd, LPARAM lParam )
{
    if (IsWindowVisible(hwnd) && hwnd != myWnd) {
        char className[256];
        GetClassName(hwnd, className, 256);

        if (strcmp(className, "WorkerW") != 0 && strcmp(className, "ShellDll_DefView") != 0) {
            ShowWindow(hwnd, SW_MINIMIZE);
        }
    }

    return TRUE;
}

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
        case WM_CREATE:
			// Счетчик C
			hCounter = CreateWindow("static", "ST_U", WS_CHILD | WS_VISIBLE | SS_CENTER, 30, 13, 40, 25, hWnd, (HMENU)NULL, hInst, NULL);
            SetWindowText(hCounter, "1");

			subButton = CreateWindow ("Button", "<", WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,  10, 10, 20, 25, hWnd, (HMENU)ID_SUB_COUNTER, hInst, 0);
            addButton = CreateWindow ("Button", ">", WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,  70, 10, 20, 25, hWnd, (HMENU)ID_ADD_COUNTER, hInst, 0);

			// Таймер
            hLabel = CreateWindow("static", "ST_U", WS_CHILD | WS_VISIBLE | SS_CENTER | WS_BORDER, 40, 70, 80, 25, hWnd, (HMENU)NULL, hInst, NULL);
			ParseTimeToString(settingTimer);
            SetWindowText(hLabel, buffer);

			rButton = CreateWindow ("Button", "R", WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,  125, 70, 25, 25, hWnd, (HMENU)ID_RETRY, hInst, 0);
			
			// Кнопка
            sButton = CreateWindow ("Button", "Go", WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,  110, 10, 70, 25, hWnd, (HMENU)ID_BUTTON, hInst, 0);
            
			// Иконки
			HICON hIcon, hIconSm;
			hIcon = LoadImage(NULL, "icon.ico", IMAGE_ICON, 64, 64, LR_LOADFROMFILE);
			hIconSm = LoadImage(NULL, "icon.ico", IMAGE_ICON, 16, 16, LR_LOADFROMFILE);
			SendMessage(hWnd, WM_SETICON, ICON_BIG, (LPARAM)hIcon);
			SendMessage(hWnd, WM_SETICON, ICON_SMALL, (LPARAM)hIconSm);

			break;
		case WM_COMMAND:
            if((LOWORD(wParam)==ID_BUTTON)&&(HIWORD(wParam)==BN_CLICKED))
            {
				if (FlagRetry) {
					start = time(NULL) + settingTimer;
					SetWindowText(sButton, "Stop");

					ParseTimeToString(settingTimer);
                	SetWindowText(hLabel, buffer);

					KillTimer(hWnd, IDT_TIMER); 
					SetTimer(hWnd, IDT_TIMER, 300, (TIMERPROC)NULL); // Таймер быстрее, чтобы не было скачков

					FlagRetry = FALSE;
					FlagStop = TRUE;
				} else if (FlagStop){
					KillTimer(hWnd, IDT_TIMER); 
					SetWindowText(sButton, "Continue");
					FlagStop = FALSE;
					FlagContinue = TRUE;

				} else if (FlagContinue){
					start = time(NULL) + lastSeconds;
					SetWindowText(sButton, "Stop");
					SetTimer(hWnd, IDT_TIMER, 300, (TIMERPROC)NULL); // Таймер быстрее, чтобы не было скачков
					FlagStop = TRUE;
					FlagContinue = FALSE;
				}
            }
			
			if ((LOWORD(wParam)==ID_SUB_COUNTER)&&(HIWORD(wParam)==BN_CLICKED)) 
			{
				if (settingTimer > 60) {
					settingTimer -= 60;
					TCHAR bufferC[64];
					sprintf(bufferC, "%ld", settingTimer/60);
					SetWindowText(hCounter, bufferC);
				}
			}

			if ((LOWORD(wParam)==ID_ADD_COUNTER)&&(HIWORD(wParam)==BN_CLICKED)) 
			{
				if (settingTimer < (24 * 60 * 60)) {
					settingTimer += 60;
					TCHAR bufferC[64];
					sprintf(bufferC, "%ld", settingTimer/60);
					SetWindowText(hCounter, bufferC);
				}

			}

			if((LOWORD(wParam)==ID_RETRY)&&(HIWORD(wParam)==BN_CLICKED))
			{
				KillTimer(hWnd, IDT_TIMER); 

				ParseTimeToString(settingTimer);
                SetWindowText(hLabel, buffer);

				FlagStop = FALSE;
				FlagRetry = TRUE;
				FlagContinue = FALSE;
				
				SetWindowText(sButton, "Go");

				// start = time(NULL) + settingTimer;

				// ParseTimeToString(settingTimer);
				// SetWindowText(hLabel, buffer);

				
				// SetTimer(hWnd, IDT_TIMER, 300, (TIMERPROC)NULL); // Таймер быстрее, чтобы не было скачков

			}
			break;
        case WM_TIMER: 
            if (wParam == IDT_TIMER)
            {
                lastSeconds = start - time(NULL);
                if (lastSeconds < 0) 
                {
                    KillTimer(hWnd, IDT_TIMER); 
                    EnumDesktopWindows(0, &EnumDesktopWindowsProc, 0);
					PlaySound("sound.wav", NULL, SND_FILENAME);
					SetWindowText(sButton, "Go");
					FlagRetry = TRUE;
                    break;
                }

				ParseTimeToString(lastSeconds);
                SetWindowText(hLabel, buffer);
            }
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProc(hWnd, message, wParam, lParam);
            break;
		
	}

	return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	// Структура класса окна
	WNDCLASSEX wcex;

	wcex.cbSize = sizeof(WNDCLASSEX);
	wcex.style          = CS_HREDRAW | CS_VREDRAW;
	wcex.lpfnWndProc    = WndProc;
	wcex.cbClsExtra     = 0;
	wcex.cbWndExtra     = 0;
	wcex.hInstance      = hInstance;
	wcex.hIcon          = LoadIcon(hInstance, IDI_APPLICATION);
	wcex.hCursor        = LoadCursor(NULL, IDC_ARROW);
	wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+11);
	wcex.lpszMenuName   = NULL;
	wcex.lpszClassName  = szClassName;
	wcex.hIconSm        = LoadIcon(wcex.hInstance, IDI_APPLICATION);
	
	// Регистрирация класса окна
	if (!RegisterClassEx(&wcex))
	{
		MessageBox(NULL, "Call to RegisterClassEx failed!", "Error!", 0);
		return 1;
	}
	
	// Создание окна
	hInst = hInstance;

	myWnd = CreateWindow(
		szClassName,
		"Pomodoro",
		WS_SYSMENU,
		CW_USEDEFAULT, CW_USEDEFAULT,
		200, 140,
		NULL,
		NULL,
		hInstance,
		NULL
	);

	if (!myWnd)
	{
		MessageBox(NULL, "Call to CreateWindow failed!", "Error!", MB_ICONASTERISK);
		return 1;
	}

	// // Прозрачность
	// SetWindowLong(myWnd, GWL_EXSTYLE, GetWindowLong(myWnd, GWL_EXSTYLE) | WS_EX_LAYERED);
	// SetLayeredWindowAttributes(myWnd, 0, (255 * 70) / 100, LWA_ALPHA);
	
	// Отображение окна
	ShowWindow(myWnd,nCmdShow);
	UpdateWindow(myWnd);

	// Цикл обработки сообщений
	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0) > 0)
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return msg.wParam;
}
