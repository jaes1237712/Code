// run with g++ -o run gsl.cpp -lgsl -lgslcblas
#include <gsl/gsl_deriv.h>
#include <gsl/gsl_sf_bessel.h>
#include <iostream>
#include <cmath>
#include <gsl/gsl_integration.h>

double mu=0; double sigma=2;
double f(double x, void * params){
    double factor_1 = 1/(sqrt(2*M_PI)*sigma);
    double fun_in_exp = -pow(x-mu,2)/(2*pow(sigma,2));
    double factor_2 = exp(fun_in_exp);
    return factor_1*factor_2;
}

/*
void ex_n4_2(){
    double x(0.5), h(1E-2);
    double fp_exact = fp(x);
    printf("Exact sol.   = %.16f\n",fp_exact);
    gsl_function F;
    F.function = &f;
    F.params = 0;

    double result, abserr;
    gsl_deriv_central(&F, x, h, &result, &abserr);
        
    printf("Numeric sol. = %.16f +- %.16f\n",result,abserr);
    printf("difference   = %.16f\n",fabs(result-fp_exact));
}
*/
//int gsl_integration_qag(const gsl_function *f, double a, double b, double epsabs, double epsrel, size_t limit, int key, gsl_integration_workspace *workspace, double *result, double *abserr)

int exercise_1(){
    gsl_integration_workspace *w = gsl_integration_workspace_alloc(1000);
    gsl_function F;
    F.function = &f;
    F.params = 0;
    double r, er;
    size_t n;
    gsl_integration_qag( &F , -1., 1., 1E-10, 1E-10,1000,GSL_INTEG_GAUSS21, w, &r, &er);
    gsl_integration_workspace_free(w);
    return r;
}

int main()
{
    return exercise_1();
}
