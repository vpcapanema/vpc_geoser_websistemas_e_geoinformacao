Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('D:\REPOSITORIOS\vpc-geoser_websistemas_e_geoinformacao\assets\identidade-visual\assinaturas-verticais\assinatura-vpc-exo2-com-slogan-transparente.png')
Write-Output "$($img.Width)x$($img.Height)"
$img.Dispose()
