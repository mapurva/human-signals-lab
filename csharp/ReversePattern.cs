using System;

class ReversePattern
{
    static string ReverseMessage(string msg)
    {
        var words = msg.Split(' ');
        Array.Reverse(words);
        return string.Join(" ", words);
    }

    static double SymmetryScore(string msg)
    {
        var original = msg.ToLower().Split(' ');
        var reversed = ReverseMessage(msg).ToLower().Split(' ');

        int matches = 0;

        for (int i = 0; i < original.Length; i++)
        {
            if (original[i] == reversed[i])
                matches++;
        }

        return (double)matches / original.Length;
    }

    static void Main()
    {
        Console.Write("Enter message: ");
        string msg = Console.ReadLine();

        Console.WriteLine("Reversed: " + ReverseMessage(msg));
        Console.WriteLine("Symmetry Score: " + SymmetryScore(msg));
    }
}