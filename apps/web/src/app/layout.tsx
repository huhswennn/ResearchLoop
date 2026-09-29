import "./globals.css";

export const metadata = {
  title: "ResearchLoop",
  description: "From Evidence to Experiment",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
