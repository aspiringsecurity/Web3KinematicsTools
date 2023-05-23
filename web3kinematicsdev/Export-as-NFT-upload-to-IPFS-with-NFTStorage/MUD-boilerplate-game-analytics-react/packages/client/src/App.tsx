import React from "react";
import "./index.css";
import {
  AppContainer,
  Container,
  Card,
  HeaderDiv,
  Subtitle,
  Title,
  Footer,
  TextLink,
} from "./theme";

export const App = () => {
  return (
    <Container>
      <AppContainer>
        <HeaderDiv>
          <Title>MUD x React Workshop</Title>
          <Subtitle>Creating a todo list using MUD</Subtitle>
        </HeaderDiv>

        <Card>
        </Card>

        <Footer>
          <TextLink href="https://v2.mud.dev">MUD docs</TextLink>
        </Footer>
      </AppContainer>
    </Container>
  );
};
