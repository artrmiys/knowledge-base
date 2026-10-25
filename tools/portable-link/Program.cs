using System.Diagnostics;
using System.Windows.Forms;

const string wikiUrl = "https://artrmiys.github.io/knowledge-base/";

try
{
    Process.Start(new ProcessStartInfo(wikiUrl) { UseShellExecute = true });
}
catch (Exception ex)
{
    MessageBox.Show(
        $"Не удалось открыть Wiki в браузере.\n\n{wikiUrl}\n\n{ex.Message}",
        "Wiki",
        MessageBoxButtons.OK,
        MessageBoxIcon.Error);
}
