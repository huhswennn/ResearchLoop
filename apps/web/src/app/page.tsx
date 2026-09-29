export default function Home() {
  return (
    <main className="shell">
      <div className="eyebrow">RESEARCHLOOP</div>
      <h1>Turn evidence into experiments.</h1>
      <p className="lead">
        Build a traceable research loop from literature and hypotheses to
        executable experiments, observations, critique, and the next iteration.
      </p>
      <div className="actions">
        <button>Discover a research question</button>
        <button className="secondary">Reproduce a paper</button>
      </div>
      <section>
        <strong>v0.1</strong>
        <span>Evidence → Hypothesis → Experiment → Run → Critic → Loop</span>
      </section>
    </main>
  );
}
