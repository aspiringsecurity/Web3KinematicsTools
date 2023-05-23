import { useState } from "react";
import { FormButton, FormField, FormFieldWrapper } from "./theme";
import { Plus } from "./theme/Plus";

export function ToDoForm() {
  const [newToDo, setNewToDo] = useState("");

  return (
    <FormFieldWrapper>
      <FormField type="text" placeholder="new todo" value={newToDo} onChange={(e) => {
        setNewToDo(e.target.value);
      }} />
      <FormButton>
        <Plus />
      </FormButton>
    </FormFieldWrapper>
  )
}