public class Solution {
    public string DefangIPaddr(string address) {
        string newAddress;
			newAddress = address.Replace(".", "[.]");
			return newAddress;
    }
}