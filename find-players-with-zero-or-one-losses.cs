public class Solution {
    public IList<IList<int>> FindWinners(int[][] matches) {
        var losses = matches.Select(x => x[1]);

        return new int[][]{
            
            matches
                .Select(x => x[0])
                .Except(losses)
                .OrderBy(x => x)
                .ToArray(),
            
            losses
                .GroupBy(x => x)
                .Where(g => g.Count() == 1)
                .Select(g => g.Key)
                .OrderBy(x => x)
                .ToArray()
        };
    }
}