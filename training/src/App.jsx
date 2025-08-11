/*
npm install -D tailwindcss@3.4.10 postcss@8.4.41 autoprefixer@10.4.20 
npx tailwindcss init -p
*/
import AddTasks from "./components/AddTasks";
import Tasks from "./components/Tasks";

function App() {
  return (
    <div className="w-screen h-screen bg-slate-500 flex justify-center p-6">
      <div className="-w[500px]">
        <h1 className="text-slate-100 text-3xl font-bold text-center">
          Gerenciador de tarefas
        </h1>
        <AddTasks />
        <Tasks />
      </div>
    </div>
  );
}

export default App;
