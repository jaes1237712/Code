#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

bool if_pirme(long long n){
    for(long long i=2;i<n;i++){
        if(n%i==0)
            return 0;
    }
    return 1;
}

long long quickpow(long long a, long long b, long long m){
    long long k=1;
    while(b>0){
        if(b&1){
            k=(k*a)%m;
        }
        b=b>>1;
        a=(a*a)%m;
    }
    return k;
}

int main(){
    std::vector<long long> primes;
    bool Date[32]={0};
    // Collect primess
    for(long long i=2; i<50; i++){
        if(if_pirme(i))
            primes.push_back(i);
    }
    long long p,q,r,e,d,n,c,N;
    long long l=primes.size();
    for(long long i=0; i<l; i++){
        for(long long k=0; k<l; k++){
            if(k==i || primes[i]*primes[k]<520)
                continue;
            // Step one and two
            p=primes[i];    q=primes[k];    r=(p-1)*(q-1);  N = p*q;
            // Step three
            for(long long j=2; j<r; j++){
                if(std::__gcd(j,r)==1){
                    e=j;
                    // Step four
                    for(long long m=2;m<r;m++){
                        if( (e*m)%r == 1){
                            d = m;
                            // Guess the date
                            for(long long b=1201;b<1232;b++) {
                                long long A = quickpow(520,d,N);
                                long long B = b%N;
                                if(A == B){
                                    Date[b-1200]=1;
                                }
                            }
                        }
                    }
                }
            }
            
        }
    }
    long long ans=0;
    for(long long i=1;i<=31;i++){
        if(Date[i])
        {
            std::cout << i+1200 <<'\n';
            ans+=1200+i;
        }
    }
    std::cout << ans <<'\n';
    return 0;
}