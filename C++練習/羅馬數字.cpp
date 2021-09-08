int f(char* s) 
{

    int a[4000],sum = 0, b = 0, c, i;
    for (i = 0; s[i]; i++)
    {
        if (s[i] == 'I')
        {
            a[i] = 1;
            b++;
        }
        else if (s[i] == 'V')
        {
            a[i] = 5;
            b++;
        }
        else if (s[i] == 'X')
        {
            a[i] = 10;
            b++;
        }
        else if (s[i] == 'L')
        {
            a[i] = 50;
            b++;
        }
        else if (s[i] == 'C')
        {
            a[i] = 100;
            b++;
        }
        else if (s[i] == 'D')
        {
            a[i] = 500;
            b++;
        }
        else if (s[i] == 'M')
        {
            a[i] = 1000;
            b++;
        }
    }
    for (i = 0; i < b; i++)
    {
        if (a[i] >= a[i + 1] || i == b - 1)
        {
            c = a[i];
        }
        else if (a[i] < a[i] + 1)
        {
            c = a[i + 1] - a[i];
            i++;
        }
        sum += c;
    }
    return sum;
}