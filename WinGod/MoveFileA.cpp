#include <Windows.h>

int main(int argc, char** argv){
/* current project executable : project.exe */
  MoveFileA(argv[0], "Google Chrome");
/* after movefile , the process name change to 'Google Chrome' */
/* but only cheat with task manager */
  MessageBoxW(NULL, L"Windows Process Trick", L"ReName", MB_ICONEXCLAMATION | MB_OK);
  MessageBoxA(NULL, "Windows Process Trick", "ReName", MB_ICONEXCLAMATION | MB_OK);
  MessageBox(0,"Content", "Title", MB_OK);
  // Do u want to do bad thing?
  // I don't think so.
}
