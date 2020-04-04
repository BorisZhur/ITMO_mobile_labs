using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public class cdr
        {
            DateTime Timestamp;
            string Origin;
            string Destination;
            float MinCount;
            int SmsCount;

        }
        public float tarificate(float callDuration, int smsNumber, int MinP1, int SmsP1, int minPriceP1, int smsPriceP1, int minPriceP2, int smsPriceP2)
        {
            float price = 0;
            if (callDuration < MinP1) { price = callDuration * minPriceP1; }
            else { price = MinP1 * minPriceP1 + (callDuration - MinP1) * minPriceP2; }
            if (smsNumber < SmsP1) { price += smsNumber * smsPriceP1; }
            else { price += SmsP1 * smsPriceP1 + (smsNumber - SmsP1) * smsPriceP2; }
            return price;
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
        
        
    }
}
