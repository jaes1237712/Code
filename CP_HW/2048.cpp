#include <iostream>
long long matrix[4][4] = {0};
void press_left()
{
    
    for(long long i=0;i<4;i++)
    {
        long long row[4] = {0}; //重排後的序列
        long long count = 0;  //從左往右數第幾個    
        for(long long j=0; j<4; j++)
        {
            if(matrix[i][j]!=0)
            {
                row[count] = matrix[i][j];
                count++;
            }
        }
        for(long long j=0; j<3; j++)
        {
            if(row[j]==0)
                break;
            if(row[j]==row[j+1])
            {
                row[j] = row[j]+row[j+1];
                row[j+1] = 0;
                long long temp = j+1;     //把剩下的往左推
                while(row[temp]==0 && temp<3)
                {
                    if(row[temp+1]!=0)
                    {
                        row[temp] = row[temp+1];
                        row[temp+1] = 0;
                    }
                    else
                        break;
                    temp++;
                }
            }
        }
        // 把row替換進去
        for(long long j=0; j<4; j++)
            matrix[i][j] = row[j];
    }
}
void press_down()
{
    for(int i=0;i<4;i++)
    {
        int row[4] = {0};
        int count = -1;
        for(int j=3; j>=0; j--)
        {
            if(matrix[j][i]!=0)
            {
                count++;
                row[count] = matrix[j][i];
            }
        }
        for(long long j=0; j<3; j++)
        {
            if(row[j]==0)
                break;
            if(row[j]==row[j+1])
            {
                row[j] = row[j]+row[j+1];
                row[j+1] = 0;
                long long temp = j+1;     //把剩下的往左推
                while(row[temp]==0 && temp<3)
                {
                    if(row[temp+1]!=0)
                    {
                        row[temp] = row[temp+1];
                        row[temp+1] = 0;
                    }
                    else
                        break;
                    temp++;
                }
            }
        }
        for(int j=3;j>=0;j--)
            matrix[j][i]=row[3-j];
    }
}
void press_right()
{
    for(int i=0;i<4;i++)
    {
        int row[4] = {0};
        int count = -1;
        for(int j=3; j>=0; j--)
        {
            if(matrix[i][j]!=0)
            {
                count++;
                row[count] = matrix[i][j];
            }
        }
        for(long long j=0; j<3; j++)
        {
            if(row[j]==0)
                break;
            if(row[j]==row[j+1])
            {
                row[j] = row[j]+row[j+1];
                row[j+1] = 0;
                long long temp = j+1;     //把剩下的往左推
                while(row[temp]==0 && temp<3)
                {
                    if(row[temp+1]!=0)
                    {
                        row[temp] = row[temp+1];
                        row[temp+1] = 0;
                    }
                    else
                        break;
                    temp++;
                }
            }
        }
        for(int j=3;j>=0;j--)
            matrix[i][j]=row[3-j];
    }
}
void press_up()
{
    for(long long i=0;i<4;i++)
    {
        long long row[4] = {0}; //重排後的序列
        long long count = 0;  //從上往下數第幾個    
        for(long long j=0; j<4; j++)
        {
            if(matrix[j][i]!=0)
            {
                row[count] = matrix[j][i];
                count++;
            }
        }
        for(long long j=0; j<3; j++)
        {
            if(row[j]==0)
                break;
            if(row[j]==row[j+1])
            {
                row[j] = row[j]+row[j+1];
                row[j+1] = 0;
                long long temp = j+1;     //把剩下的往上推
                while(row[temp]==0 && temp<3)
                {
                    if(row[temp+1]!=0)
                    {
                        row[temp] = row[temp+1];
                        row[temp+1] = 0;
                    }
                    else
                        break;
                    temp++;
                }
            }
        }
        // 把row替換進去
        for(long long j=0; j<4; j++)
            matrix[j][i] = row[j];
    }
}

long long sum()
{
    long long total = 0;
    for(long long i=0; i<4; i++)
        for(long long j=0; j<4; j++)
            total += matrix[i][j];
    return total;
}
int main()
{
    long long round = 0;
    while(1!=0)
    {
        long long seed = (round*round*round)%16;
        long long x = (seed-(seed%4))/4;
        long long y = seed%4;
        bool flag = 1;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(matrix[i][j]==0)
                    flag = 0;
            }
        }
        if(flag)
        {
            std::cout<<"END:"<<sum()<<'\n';
            return 0;
        }
        while(matrix[x][y]!=0) 
        {
            seed = (seed+1)%16;
            x = (seed-(seed%4))/4;
            y = seed%4;
            if(x>3||y>3)
            {
                x=0;
                y=0;
            }
        }
        if(matrix[x][y]==0)
            matrix[x][y] = 2;
        std::cout <<"-----------------round="<< round <<"  sum="<<sum()<<"  (x,y)="<<x<<","<<y<<'\n'; // 初始長怎樣
        for(long long i=0; i<4; i++)
        {
            for(long long j=0; j<4; j++)
                std::cout << matrix[i][j]<<" ";
            std::cout << '\n';
        }
        switch (round%4)
        {
            case 0:
                std::cout<<"press_left"<<'\n';
                press_left();
                break;
            case 1:
                std::cout<<"press_down"<<'\n';
                press_down();
                break;
            case 2:
                std::cout<<"press_right"<<'\n';
                press_right();
                break;
            case 3:
                std::cout<<"press_up"<<'\n';
                press_up();
                break;
        }
        round++;
        for(long long i=0; i<4; i++)
        {
            for(long long j=0; j<4; j++)
                std::cout << matrix[i][j]<<" ";
            std::cout << '\n';
        }
    }
    return 0;
}