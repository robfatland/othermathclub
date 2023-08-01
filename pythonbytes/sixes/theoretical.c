// 
// TN_theory.c: 
// Theoretical solutions of the <T(N)> problem.
//
// Compile using
// % gcc -o TN_theory TN_theory.c -lm
//
// Given N dice, how many throws should be necessary (expectation) before
// all of them have turned up 6 at least once? The 'game' version is identical
// but permits the player to remove any dice showing '6' after each throw,
// giving a sense of progress towards the goal of getting all the dice
// showing 6.
//
// The calculation is straightforward although the factors involved required
// some thought on my part. First the approach will be to sum over possible
// throws, the variable t, which should run from 1 to infinity. 
// 
// For each pending throw there is a certain probability that this throw will
// end the game.  This probability is a density function or pdf(t). It is 
// therefore normalized. Or at least it *should* be!
//
// Once the form of pdf(t) is determined, the actual sum necessary to calculate
// <T(N)> is the sum over t (from 1 to inf) of t x pdf(t). Again N is the number
// of dice we are considering in this particular game.
//
// This agrees nicely with an "experiment" run by another program. In particular
// it says that <T(1)> = 6, a nice conservation of probabilty (since we can ask 
// what is <T(1)> for rolling a 5, 4, 3, 2, or 1; all must be the same and we 
// expect to roll one of each in six throws of a single die!
//
// Lastly the form of the pdf. We suppose there are i dice remaining after t-1
// throws. These dice have never yet come up 6. The probability they will all
// come up 6 on the next throw is 6^(-i). That is the first factor, F1.
// 
// But how many ways can we choose these i dice from among N originals? The
// answer is "N choose i". This is factor two, F2.
//
// What is the probability that none of these i dice has come up 6 in t-1
// throws? Since the dice are (assumed to be) independent, the probability is the
// product of the probabilities of each die not coming up 6. Call this Pn6(t-1).
// The probability of all i dice not coming up 6 is Pn6(t-1)^i.
//
// There are 6^(t-1) ways of throwing a die t-1 times and 5^(t-1) ways of doing this
// without rolling 6. Thus Pn6(t-1) = (5/6)^(t-1). This and the previous paragraph
// give us the probability that our i chosen dice were thrown t-1 times and never
// came up 6. This the third factor F3 = ((5/6)^(t-1))^i.
//
// Lastly we need to ensure that the remaining N-i dice came up 6 at least once.
// As for F3, we take P(1 die came up 6 at least once) and raise it to the (N-i) power.
// P(die came up 6 at least once in t-1 throws) = 1 - P(die never came up 6 in t-1 throws). 
// This is the same as the idea in F3. So F4 is (1 - (5/6)^(t-1))^N-i.
//
// pdf(t, i) = F1 * F2 * F3 * F4.
//
// The full pdf must sum over all possible values of i, which is from 1 to N.
//
// <T(N)> = Sum(t = 1 to inf) { t * Sum(i = 1 to N) { F1 * F2 * F3 * F4 } }
//
// That's it. I don't know how far this can be simplified.
//
// The simple formula values provided are derived from this argument: Suppose we have 
// N dice and every time they are rolled, one sixth of them are removed. This can be
// done--we assume--even if the remainder includes fractions of a die. Once we get down
// to 1/2 a die, since the dice are in fact quantized, we must be finished since 1/2
// a die is really no dice. Interestingly this simple formula does a decent job for
// ten or more dice, say, although after N = 20 the estimate is consistently a bit high.
//


#include <math.h>

double a_choose_b(double a, double b);

main(int argc, char **argv)
{
  double d_five_sixths = 5./6.;
  double d_one_sixth   = 1./6.;
  int t;
  int i;
  int N, upper_N;
  double d_T;
  double d_N, d_i, d_t;
  double d_pdf_sum, d_pdf_delta;
  double Nmorsalo;
  double d_pdf_1, d_pdf_1_sum;
  double inrs;
  double d_expT_sum;
  double d_simple_formula;

  printf ("\n");
  printf ("TN_theory [N-high]\n");
  printf ("\n");
  printf ("TN_theory: Print out theoretical values of <T(N)> for     \n");
  printf ("N = 1, 2, 3, ..., N-high, where N-high is either given    \n");
  printf ("on the command line or by default is 5. These values      \n");
  printf ("are the expected number of throws to cause N dice to      \n");
  printf ("come up 6 at least once, when all N are thrown repeatedly \n");
  printf ("en masse.                                                 \n");
  printf ("\n");
  upper_N = argc > 1 ? atoi(argv[1]) : 5;

  for (N = 1; N <= upper_N; N++) {
    d_N = (double)N;

    for (t = 1, d_pdf_sum = 0., d_expT_sum = 0., d_pdf_1_sum = 0.; t < 100; t++) {
      d_t = (double)t;
      for (i = 1, d_pdf_delta = 0.; i <= N; i++) { 
        d_i           = (double)i;
        Nmorsalo      = pow(1. - pow(d_five_sixths, d_t - 1.), d_N - d_i);
        inrs          = pow(pow(d_five_sixths, d_t - 1.), d_i);
        d_pdf_delta  += a_choose_b(d_N, d_i)*pow(d_one_sixth, d_i)*inrs*Nmorsalo;
      }
      d_pdf_sum  += d_pdf_delta;
      d_expT_sum += d_t * d_pdf_delta;

      // The following is used to check the N = 1 case using the simplified pdf
      // d_pdf_1      = d_one_sixth * pow(d_five_sixths, d_t - 1.);
      // d_pdf_1_sum += d_pdf_1;
      // printf ("N %d t %d pdf_delta is %lf, sum %lf    single pdf_delta %lf, sum %lf. Diff %lf.\n",
      //   N, t, d_pdf_delta, d_pdf_sum, d_pdf_1, d_pdf_1_sum, d_pdf_sum - d_pdf_1_sum);
    }
    d_simple_formula = log(d_N / 0.5) / log(6./5.);

    printf ("N = %4d: pdf sum is %lf, <T(N)> = %lf, simple formula gives %lf.\n",
      N, d_pdf_sum, d_expT_sum, d_simple_formula);
  }
}

// This is a simple function to calculate A-choose-B; it accumulates the factorial
// products in the simplest way possible. For this reason it will not handle very
// large numbers.
double a_choose_b(double a, double b)
{
  double d_acb;
  double d_i;
  double d_num, d_den_a, d_den_b;

  if      (a == 0. || a == 1.          ) { d_acb = 1.; } 
  else if (b == 0. || b == a           ) { d_acb = 1.; }
  else if (a <  0. || b  < 0. || b > a) {
    printf("C(a,b) error %lf %lf halting.\n\n", a, b);
    exit(-1);
  } 
  else {
    for (d_num   = 1., d_i = 2.; d_i <= a    ; d_i += 1.) { d_num   *= d_i; }
    for (d_den_a = 1., d_i = 2.; d_i <= b    ; d_i += 1.) { d_den_a *= d_i; }
    for (d_den_b = 1., d_i = 2.; d_i <= a - b; d_i += 1.) { d_den_b *= d_i; }
    d_acb = d_num / (d_den_a * d_den_b);
  }
  return d_acb;
}
