type Ingredient = {
    id: string;
    name: string;
  };
  
  type Inventor = {
    id: string;
    firstName: string;
    lastName: string;
  };
  
  type Difficulty =
    | "Unknown"
    | "Advanced"
    | "Moderate"
    | "Beginner"
    | "OrdinaryWizardingLevel"
    | "OneOfAKind";
  
  type Elixir = {
    id: string;
    name: string;
    effect: string;
    sideEffects: string;
    characteristics: string;
    time: string;
    difficulty: Difficulty;
    ingredients: Ingredient[];
    inventors: Inventor[];
    manufacturer: string;
  };
  
  type Spell = {
    id: string;
    name: string;
    incantation: string;
  };
  
  const Endpoints = {
    ELIXIRS: "Elixirs",
    SPELLS: "Spells",
  } as const;
  
  type EndpointType = (typeof Endpoints)[keyof typeof Endpoints];
  
  let elixirs: Elixir[] = [];
  let spells: Spell[] = [];
  let validOption: string | undefined;
  
  const gameContainer = document.getElementById("game")!; 
  
  async function fetchData<T>(endpoint: EndpointType): Promise<T[]> {
    const response = await fetch(`https://wizard-world-api.herokuapp.com/${endpoint}`);
    if (!response.ok) {
      throw new Error(`Error fetching data from ${endpoint}`);
    }
    const data = await response.json();
    return data;
  }
  
  async function fetchAllData(): Promise<void> {
    const [elixirsResponse, spellsResponse] = await Promise.all([
      fetchData<Elixir>(Endpoints.ELIXIRS),
      fetchData<Spell>(Endpoints.SPELLS),
    ]);
  
    elixirs = elixirsResponse.filter((elixir) => elixir.effect);
    spells = spellsResponse.filter((spell) => spell.incantation);
  }
  
  function getRandomElements<T>(array: T[], count: number): T[] {
    const indexes: Set<number> = new Set();
  
    while (indexes.size < count) {
      const randomIndex = Math.floor(Math.random() * array.length);
      indexes.add(randomIndex);
    }
  
    return Array.from(indexes).map((index) => array[index]);
  }
  
  function generateOptions<T>(randomElements: T[]): { rightOption: T; options: T[] } {
    const [rightOption, ...rest] = randomElements;
    const options = [rightOption, ...rest].sort(() => (Math.random() > 0.5 ? 1 : -1));
    return { rightOption, options };
  }
  
  function elixirGame(): void {
    const { options, rightOption } = generateOptions(getRandomElements(elixirs, 3));
    validOption = rightOption.name;
    console.log(`Cheat Mode: Right answer is ${validOption}`);
    renderOptions(`Which elixir effect is: "${rightOption.effect}"?`, options.map((e) => e.name));
  }
  
  function spellGame(): void {
    const { options, rightOption } = generateOptions(getRandomElements(spells, 3));
    validOption = rightOption.name;
    console.log(`Cheat Mode: Right answer is ${validOption}`);
    renderOptions(`Which spell incantation is: "${rightOption.incantation}"?`, options.map((s) => s.name));
  }
  
  function renderOptions(question: string, answers: string[]): void {
    const questionElement = document.getElementById("question");
  
    if (!gameContainer || !questionElement) {
      throw new Error("Game container or question element not found");
    }
  
    gameContainer.innerHTML = "";
    questionElement.textContent = question;
  
    answers.forEach((answer) => {
      const option = document.createElement("button");
      option.textContent = answer;
      gameContainer.appendChild(option);
    });
  }
  
  gameContainer.addEventListener("click", (event: MouseEvent) => {
    const target = event.target as HTMLElement;
  
    if (target.tagName === "BUTTON") {
      const selectedOption = target.textContent;
  
      if (selectedOption === validOption) {
        round();
      } else {
        alert("Wrong answer!");
      }
    }
  });
  
  function round(): void {
    const randomGame = Math.random() > 0.5 ? elixirGame : spellGame;
    randomGame();
  }
  
  async function startGame(): Promise<void> {
    await fetchAllData();
    round();
  }
  
  startGame();
  