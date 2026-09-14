import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://vpc-websistemas.com.br"),
  title: "VPC-WEBSISTEMAS E GEOINFORMAÇÃO",
  description: "Soluções digitais sob medida para território, infraestrutura e dados públicos, com governança de dados como base da concepção à operação.",
  applicationName: "VPC-WEBSISTEMAS E GEOINFORMAÇÃO",
  authors: [{ name: "VPC-WEBSISTEMAS E GEOINFORMAÇÃO" }],
  keywords: ["geoprocessamento", "sensoriamento remoto", "WebGIS", "websistemas", "análise de dados", "soluções sob medida"],
  openGraph: {
    type: "website",
    locale: "pt_BR",
    siteName: "VPC-WEBSISTEMAS E GEOINFORMAÇÃO",
    title: "VPC-WEBSISTEMAS E GEOINFORMAÇÃO",
    description: "Soluções digitais sob medida que transformam dados, território e processos em sistemas operacionais, com governança de dados como base.",
    url: "https://vpc-websistemas.com.br",
    images: [{ url: "/og-vpc.png", width: 1200, height: 630, alt: "VPC-WEBSISTEMAS E GEOINFORMAÇÃO" }],
  },
  robots: { index: true, follow: true },
  icons: { icon: "/favicon.ico", apple: "/apple-touch-icon.png" },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="pt-BR"><body>{children}</body></html>;
}
