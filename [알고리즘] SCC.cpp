#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
string* address;
int n;
stack<string> stck;

// 인접 리스트 : G
vector<string> G[1001];
// 인접 리스트 : G+
vector<string> G_Reverse[1001];

// DFS1용 방문 정보
bool ch1[1001] = {false, };
// DFS2용 방문 정보
bool ch2[1001] = {false, };

// 중간 정보를 가지는 배열
string temp[1001];
// 각 주소의 리더의 주소를 나타 내는 배열
string ans[1001];

// 각 주소와 매핑 되는 인덱스 변환 해주는 함수
int search(int n, string cur) {
    for (int i = 0; i < n; ++i) {
        if (address[i] == cur)
            return i;
    }
}

// 스택에 넣을 첫번째 DFS
void DFS1(string addr) {
    int idx = search(n,addr);
    // 이미 방문 했으면 종료
    if(ch1[idx]) return;
    ch1[idx] = true;

    // 현 정점과 인접한 정점들 방문
    if (G[idx].size() != 0){
        for (int i = 0; i < G[idx].size(); ++i) {
            DFS1(G[idx][i]);
        }
    }

    // 인접한 정점들 방문 다 하고 현 정점 스택에 넣어주기
    stck.push(addr);
}

// 두번째 DFS
void DFS2(string addr, string leader) {
    int idx = search(n, addr);

    // 이미 방문했으면 종료
    if(ch2[idx]) return;
    ch2[idx] = true;

    // 현 정점의 인접한 정점이 있으면 해당 정점들 방문
    if (G_Reverse[idx].size() != 0){
        for (int i = 0; i < G_Reverse[idx].size(); ++i) {
            DFS2(G_Reverse[idx][i], leader);
        }
    }

    // 인접한 정점들 방문 다 종료 후 현 주소의 리더 정보 넣기
    ans[idx] = leader;
}

int main() {
    cin >> n;
    address = new string[n];
    // 각 주소 정보 입력 및
    // G에서의 각 인덱스와 그 인덱스에 매핑되는 주소 정보를 가지는 배열 address 초기화 및 정렬
    for (int i = 0; i < n; ++i) {
        string cur;
        cin >> cur;
        address[i] = cur;
    }
    sort(address,address+n);

    // 각 정보들 입력 받고 그래프 G 생성
    for (int i = 0; i < n; ++i) {
        string cur;
        cin >> cur;
        int idx = search(n, cur);
        int num;
        cin >> num;

        for (int j = 0; j < num; ++j) {
            string vertex;
            cin >> vertex;
            G[idx].push_back(vertex);
        }
    }
    // G에서 각 정점의 인접한 정점들 사전 순으로 정렬
    for (int i = 0; i < n; ++i) {
        sort(G[i].begin(), G[i].end());
    }

    // 사전 순으로 DFS1 수행
    for (int i = 0; i < n; ++i) {
        if (!ch1[i]) {
            DFS1(address[i]);
        }
    }

    // 스택에 삽입된 순서대로 temp에 주소 저장
    int idx = n-1;
    while (!stck.empty()) {
        temp[idx] = stck.top();
        stck.pop();
        idx--;
    }

    // G의 edge 방향 반대로 하는 그래프 G_Reverse 생성
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < G[i].size(); ++j) {
            int idx = search(n, G[i][j]);
            G_Reverse[idx].push_back(address[i]);
        }
    }

    // G_Reverse의 각 정점의 인접한 정점들 사전 순으로 정렬
    for (int i = 0; i < n; ++i) {
        sort(G_Reverse[i].begin(), G_Reverse[i].end());
    }

    // 스택에 TOP부터 차례대로 DFS 수행
    for (int i = n-1; i >= 0; --i) {
        string cur = temp[i];
        int idx = search(n, cur);
        if (!ch2[idx]) {
            DFS2(cur, cur);
        }
    }

    // 스택에 삽입된 순서로 주소 출력
    for (int i = 0; i < n; ++i) {
        cout << temp[i] << " ";
    }
    cout << endl;

    // 각 정점의 SCC의 리더가 가리키는 주소 출력
    for (int i = 0; i < n; ++i) {
        cout << ans[i] << " ";
    }
}


