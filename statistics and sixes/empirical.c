//
// DiceStudy.c
// Program to empirically estimate the number of throws of ND dice
// necessary (or *expected*) to ensure that each of the ND dice has 
// come up a '6' at least once. This expectation value for the number
// of throws necessary is abbreviated <T>.
//
// compile command: cc -o DiceStudy DiceStudy.c -lm
// run command:     DiceStudy 1 21 2
// This will give estimates of <T> for ND = 1, 3, 5, ..., 21
// The results will be printed and saved to the file DiceStudy.output.
//
// How this program works:
//   Loop over the trials, setting ND for each trial.
//     This trial: We have a number of dice ND.
//     We will play the game G times as follows:
//       Throw all ND dice.
//       Any that come up 6 are removed from the group.  
//       The remainder dice are thrown again.
//       Procedure repeats until all ND dice are eliminated.
//       We count the number of throws this required, call this T1.
//       Perform the experiment again to obtain T2, again T3, T4, ...
//         ..., TG. Take the average of G games to get <T> for ND.
// 
// After each trial the program prints a diagnostic, including <T(ND)>.
// To find out what is meant by 'theory' see the web page on this subject.
// A very rough method is suggested for calculating <T> which results in
// the 'theory' result. (It's quite a *bad* theory!)
//
// We make sure the program runs fairly quickly using this macro:
// SIZE_PER_RUN = G x ND 

#define SIZE_PER_RUN (5000000)

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

main(int argc, char **argv)
{
  long int Trials, Rolls, Ndice, sum, maxR, minR;
  int      T;
  int      ND;
  int      i;
  int      Nsix;
  int      start, stop, increment;
  float    theory;
  float    experiment, ratio;
  FILE     *fp;

  if (argc < 4) {
    printf ("\nDiceStudy start stop increment\n");
    printf ("\n");
    printf ("First trial:  Use (ND = start)             dice.\n");
    printf ("Second trial: Use (ND = start + increment) dice.\n");
    printf ("...etcetera...");
    printf ("Final trial:  Use (ND = stop)              dice.\n");
    printf ("\n");
    printf ("Results are written to file DiceStudy.output\n");
    printf ("\n");
    printf ("\n");
    exit(0);
  }

  start     = atoi(argv[1]);
  stop      = atoi(argv[2]);
  increment = atoi(argv[3]);

  fp = fopen("DiceStudy.output", "w");
  fclose(fp);

  for (ND = start; ND <= stop; ND += increment) {

    T = SIZE_PER_RUN / ND;

    for (Trials = 0, sum = 0, maxR = 0, minR = 50000; Trials < T; Trials++) {

      Rolls = 0;
      Ndice = ND;
      while (Ndice) {
        Rolls++;
        for (i = 0, Nsix = 0; i < Ndice; i++) { if (!(random()%6)) { Nsix++; } }
        Ndice -= Nsix;
      }
      sum += Rolls;
      if (Rolls > maxR) { maxR = Rolls; }
      if (Rolls < minR) { minR = Rolls; }
    }

    theory     = log(1./(float)(2*ND)) / log(5./6.);
    experiment = (float)(sum) / (float)(T);
    ratio      = experiment / theory;

    printf("%5d   %7.4f   %7.4f   %8.7f   %5d   %5d\n", ND, experiment, theory, ratio, maxR, minR);
    fp = fopen("DiceStudy.output", "a");
    fprintf(fp, "%5d   %7.4f   %7.4f   %8.7f   %5d   %5d\n", ND, experiment, theory, ratio, maxR, minR);
    fclose(fp);

  }

  printf("\nDiceStudy: s.c.\n\n");
  exit(0);
}
